from __future__ import annotations  # Enables the use of modern type hinting features.
from os import name
from pathlib import Path
from tabnanny import verbose
from typing import Dict, Tuple, Optional, List, Callable, Any   # For type hinting. This maybe unused in this snippet but is useful for larger projects.
import logging # Logging is simply a way for your program to print messages about what it is doing, in a more controlled and professional way than using print().

# --- IfcOpenShell imports---
import ifcopenshell 
import ifcopenshell.util as util
import ifcopenshell.util.element as uel
import ifcopenshell.util.placement as up
import ifcopenshell.geom as geom

#--- Other useful imports ---
import math
from pprint import pprint
from collections import Counter, defaultdict

def extract_spaces_with_area(arch_model, *, verbose=True):
    """
    Extracts area, name, and IFC ID for each IfcSpace in an IFC model.

    Parameters
    ----------
    arch_model : ifcopenshell.file
        The ARCH model (or any IFC file containing IfcSpace).
    verbose : bool
        If True, prints each space as in your original snippet.

    Returns
    -------
    list of dict
        [
            {
                "id": int,
                "name": str,
                "area": float or None,
                "source": "Qto_SpaceBaseQuantities" | "Dimensions" | None
            },
            ...
        ]
    """
    results = []
    Spaces = arch_model.by_type("IfcSpace")

    for space in Spaces:
        psets = uel.get_psets(space)
        area = None
        source = None
        area_type = None

        # 1) Preferred: standard IFC base quantities
        if "Qto_SpaceBaseQuantities" in psets:
            qto = psets["Qto_SpaceBaseQuantities"]
            area = qto.get("NetFloorArea")
            source = "Qto_SpaceBaseQuantities"
            area_type = "Net Floor Area"    

            if area is None:
                logging.info("NetFloorArea not found, trying GrossFloorArea")
                area = qto.get("GrossFloorArea")  # fallback gross
                if area is not None:
                    source = "Qto_SpaceBaseQuantities (Gross)"
                    area_type = "Gross Floor Area"

        # 2) Fallback: Revit-like Dimensions Pset
        if area is None and "Dimensions" in psets:
            area = psets["Dimensions"].get("Area")
            if area is not None:
                source = "Dimensions"
                area_type = "Revit Dimensions Area"
        if area is None:
            logging.info("No area found for space id %s in either Qto_SpaceBaseQuantities or Dimensions. Manual check required.",
                space.id())

        # 3) Basic identification
        name = getattr(space, "LongName", None) or getattr(space, "Name", "Unnamed")
        space_id = space.id()

        if verbose:
            print(
                f"Space ID: {space_id} | "
                f"Name: {name} | "
                f"Area: {area if area is not None else 'No area found'} m²"
            )

        results.append({
            "id": space_id,
            "name": name,
            "area": area,
            "source": source,
            "area_type": area_type
        })

    return results