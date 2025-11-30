import math
import ifcopenshell
import csv
from typing import Dict, Tuple, Optional, List, Callable, Any
from pathlib import Path
import logging
from SpaceAreas import extract_spaces_with_area
from Occupants import count_chairs_by_space, apply_br18_occupancy, guess_annex_c_category, ANNEX_C_OCCUPANT_DENSITY
from BuildingCodes import choose_ieq_category, choose_pollution_class, ventilation_rate_method_1

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
def ask_for_ifc_paths():
    print("Enter paths to your IFC files (press Enter to use defaults).")

    mep_default = "25-08-D-MEP.ifc"
    arch_default = "25-08-D-ARCH.ifc"

    raw_mep = input(f"MEP IFC path [{mep_default}]: ").strip()
    raw_arch = input(f"ARCH IFC path [{arch_default}]: ").strip()

    # Strip surrounding " or ' from copy-pasted paths
    def clean(p: str, default: str) -> str:
        if not p:
            return default
        return p.strip().strip('"').strip("'")

    mep_path = clean(raw_mep, mep_default)
    arch_path = clean(raw_arch, arch_default)

    return mep_path, arch_path


def load_ifc_models(mep_path: str | Path, arch_path: str | Path) -> Tuple[ifcopenshell.file, ifcopenshell.file, Dict[str, str]]:
    """
    Load MEP and ARCH IFC models and report schema info.

    Parameters
    ----------II
    mep_path : str | Path
        Path to the MEP IFC file.
    arch_path : str | Path
        Path to the ARCH IFC file.
    echo_util_dir : bool
        If True, logs the attributes available under `ifcopenshell.util`
        (similar to your `print(dir(ifcopenshell.util))`).

    Returns
    -------
    (mep, arch, info) : tuple
        - mep: ifcopenshell.file for the MEP model
        - arch: ifcopenshell.file for the ARCH model
        - info: dict with basic metadata (schemas, paths)
    """
    mep_path = Path(mep_path)
    arch_path = Path(arch_path)

    if not mep_path.is_file():
        raise FileNotFoundError(f"MEP IFC file not found: {mep_path}")
    if not arch_path.is_file():
        raise FileNotFoundError(f"ARCH IFC file not found: {arch_path}")
    
    logging.info(f"Opening MEP IFC model from: {mep_path}")
    MEP = ifcopenshell.open(str(mep_path))

    logging.info(f"Opening ARCH IFC model from: {arch_path}")
    ARCH = ifcopenshell.open(str(arch_path))

    logging.info(f"MEP schema: {MEP.schema}")
    logging.info(f"ARCH schema: {ARCH.schema}")

    return MEP, ARCH

def simple_br18_fallback(space_entry):
    """
    BR18 fallback occupancy when there are NO chairs in the space.

    - Only apply fallback if we can guess an ANNEX C category.
    - Otherwise: 0 occupants (e.g. toilets, corridors, storage).
    """
    area = space_entry.get("area")
    if area is None or area <= 0:
        return 0

    category = guess_annex_c_category(space_entry)
    if category is None:
        if area > 200:
            logging.info(
                "Large space with no occupancy found: "
                f"Name='{space_entry.get('space_name')}', "
                f"ID={space_entry.get('space_id')}, "
                f"Area={area:.1f} m². Please check occupancy manually."
            )
        # No Annex C match → treat as 0 occupants
        return 0

    m2_per_person = ANNEX_C_OCCUPANT_DENSITY.get(category)
    if not m2_per_person:
        return 0

    # BR18: persons = area / (m² per person), rounded up
    return math.ceil(area / m2_per_person)



def main():
    # 1) Input IFC paths
    mep_path, arch_path = ask_for_ifc_paths()

    # 2) Load Ifc models
    mep, arch = load_ifc_models(mep_path, arch_path)

    # 3) Ask once for IEQ and pollution categories (for the whole building)
    ieq_category = choose_ieq_category()       # e.g. "II"
    pollution_class = choose_pollution_class()  # e.g. "LPB-2"

    # 4) Get space areas from ARCH model
    spaces_area = extract_spaces_with_area(arch, verbose=False)
    area_by_id = {s["id"]: s for s in spaces_area}

    # 5) Count chairs (occupants) per space
    spaces_chairs = count_chairs_by_space(arch, verbose=False)

    # Attach area (from SpaceAreas) to each space so fallback can use it
    for space in spaces_chairs:
        space_id = space["space_id"]
        area_info = area_by_id.get(space_id)

        if area_info is not None:
            space["area"] = area_info["area"]
            # Optionally override the name with the one from area extraction
            if area_info.get("name"):
                space["space_name"] = area_info["name"]
        else:
            space["area"] = None

    # 6) Apply simple BR18-style fallback where there are no chairs
    spaces_with_occupants = apply_br18_occupancy(
        spaces_chairs,
        br18_fallback=simple_br18_fallback,
        verbose=False,
    )

    # 7) Build CSV data

    rows = []

    # First two "info" rows
    rows.append([
        "Building Pollution Category",  # Column 1
        pollution_class,               # Column 2
        "", "", "", "", "",            # Fill remaining columns
    ])
    rows.append([
        "Indoor Air Quality Category",  # Column 1
        ieq_category,                  # Column 2
        "", "", "", "", "",
    ])

    # Header row
    rows.append([
        "Numbering",               # Column 1
        "Space ID",                # Column 2
        "Space Name",              # Column 3
        "Area [m²]",               # Column 4
        "Occupancy [persons]",     # Column 5
        "Source of Occupancy",     # Column 6
        "Calculated Vent Rates [L/s]",  # Column 7
    ])

    # Data rows – one per space
    numbering = 1
    for space in spaces_with_occupants:
        space_id = space.get("space_id")
        name = space.get("space_name") or ""
        area = space.get("area")
        occupants = space.get("final_occupants", 0)
        source = space.get("occupant_source", "")

        # Ensure area is a float for the ventilation function
        area_value = float(area) if area is not None else 0.0

        q_tot = ventilation_rate_method_1(
            occupants=occupants,
            area=area_value,
            ieq_category=ieq_category,
            pollution_class=pollution_class,
        )

        rows.append([
            numbering,
            space_id,
            name,
            area if area is not None else "",
            occupants,
            source,
            round(q_tot, 2),
        ])

        numbering += 1

    # 8) Write CSV file
    output_path = Path("ventilation_results.csv")
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)  # default delimiter = ","
        writer.writerows(rows)

    print(f"CSV written to: {output_path.resolve()}")


if __name__ == "__main__":
    main()
