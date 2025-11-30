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


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")



def classify_assembly_status(entity):
    """
    Classifies an Ifc element's decomposition role.

    Returns one of:
      - "sub-element"   → entity.Decomposes exists
      - "assembly"      → entity.IsDecomposedBy exists
      - "standalone"    → neither

    Also returns parent/children objects when relevant.
    """
    if getattr(entity, "Decomposes", None):
        parent = entity.Decomposes[0].RelatingObject
        return "sub-element", parent, None

    if getattr(entity, "IsDecomposedBy", None):
        children = entity.IsDecomposedBy[0].RelatedObjects
        return "assembly", None, children

    return "standalone", None, None




def _get_furniture_predefined_type(entity) -> Optional[str]:
    """Return PredefinedType from the instance or its type, if present."""
    # Instance-level PredefinedType
    Furniture = getattr(entity, "PredefinedType", None)
    if isinstance(Furniture, str) and Furniture:
        return Furniture

    # Type-level PredefinedType (IfcRelDefinesByType)
    if getattr(entity, "IsTypedBy", None):
        rel = entity.IsTypedBy[0]
        if getattr(rel, "RelatingType", None):
            t = rel.RelatingType
            tp = getattr(t, "PredefinedType", None)
            if isinstance(tp, str) and tp:
                return tp
    return None


def _looks_like_chair(entity, chair_keywords: Tuple[str, ...]) -> bool:
    """Heuristics to decide if an IfcFurniture element is a chair."""
    if not entity.is_a("IfcFurniture"):
        return False

    # 1) Use PredefinedType (instance or type) if available
    ptype = _get_furniture_predefined_type(entity)
    if isinstance(ptype, str) and ptype.upper() == "CHAIR":
        return True

    # 2) Text search in Name / ObjectType
    name = (getattr(entity, "Name", "") or "").upper()
    objtype = (getattr(entity, "ObjectType", "") or "").upper()
    hay = f"{name} {objtype}"
    keywords_upper = [kw.upper() for kw in chair_keywords]  # make uppercase list

    for kw in keywords_upper:
        if kw in hay:
            return True

    return False



def _is_assembly_child(entity) -> bool:
    role, _, _ = classify_assembly_status(entity)
    return role == "sub-element"

def count_chairs_by_space(
    arch_model,
    *,
    chair_keywords: Tuple[str, ...] = ("CHAIR", "SEAT"),
    exclude_assembly_children: bool = True,
    verbose: bool = True,
):
    """
    Count chairs per IfcSpace using spatial containment relations.

    Intended use:
      - Occupancy per space = number of chairs found.
      - If zero chairs, downstream logic can fall back to BR18 / DS (later integration).

    Parameters
    ----------
    arch_model : ifcopenshell.file
        The IFC containing spaces/furniture.
    chair_keywords : tuple[str, ...]
        Text keywords to match chairs when PredefinedType is missing.
    exclude_assembly_children : bool
        If True, skip furniture that are sub-elements of an assembly to avoid double counts.
    verbose : bool
        If True, print a readable summary per space.

    Returns
    -------
    list[dict]
        One entry per space:
        {
          "space_id": int,
          "space_name": str,
          "space_number": str | None,
          "chair_count": int,
          "chairs": [
              {
                "id": int,
                "GlobalId": str,
                "Name": str | None,
                "PredefinedType": str | None
              }, ...
          ]
        }
    """
    spaces = arch_model.by_type("IfcSpace")
    rels = arch_model.by_type("IfcRelContainedInSpatialStructure")

    # Mapping spaces to list of related elements 
    contained: Dict[int, List] = defaultdict(list) #defaultdict is a special dictionary that if the key does not exist, it creates it with a default value (here an empty list).
    for rel in rels:
        sp = rel.RelatingStructure
        if sp and sp.is_a("IfcSpace"):
            contained[sp.id()].extend(rel.RelatedElements or []) #sp.id() is int. Contrains the space id as a key and the related elements (which are a lot of them IfcWalls, IfcSlabs, IfcFurnitures, etc) as values in a list.
        
    results = []
    if verbose:
        print(f"Total Spaces: {len(spaces)}")

    for sp in spaces:
        sp_id = sp.id()
        name = getattr(sp, "Name", None)
        if not name or not name.strip():
            space_name = "(Unnamed Space)"
        else:
            space_name = name
        space_number = getattr(sp, "LongName", None) or getattr(sp, "Number", None) or None

        chairs_in_space = []
        seen = set()  # deduplicate by GlobalId in case of duplicates in model relations

        for el in contained.get(sp_id, []):
            if not el.is_a("IfcFurniture"):
                continue
            if exclude_assembly_children and _is_assembly_child(el):
                # skip parts of assemblies to avoid counting sub-components
                continue
            if not _looks_like_chair(el, chair_keywords):
                continue

            gid = getattr(el, "GlobalId", None)
            if gid and gid in seen:
                continue
            seen.add(gid)

            chairs_in_space.append({
                "id": el.id(),
                "GlobalId": getattr(el, "GlobalId", None),
                "Name": getattr(el, "Name", None),
                "PredefinedType": _get_furniture_predefined_type(el),
            })

        entry = {
            "space_id": sp_id,
            "space_name": space_name,
            "space_number": space_number,
            "chair_count": len(chairs_in_space),
            "chairs": chairs_in_space,
            # convenience for the later pipeline:
            "inferred_occupants": len(chairs_in_space),
            "had_any_chairs": len(chairs_in_space) > 0,
        }

        if verbose:
            header_num = f"[{space_number}]" if space_number else ""
            print(f"\nSpace: {space_name} {header_num}")
            print(f"  Chairs found: {entry['chair_count']}")
            for c in chairs_in_space:
                print(
                    f"    - ID: {c['id']} | GlobalId: {c['GlobalId']} | "
                    f"Name: {c['Name']} | PredefinedType: {c['PredefinedType'] or 'N/A'}"
                )

        results.append(entry)

    # If literally no chairs in the entire model, this may indicate a modeling pattern
    # where furniture isn't contained by spaces. You can handle that upstream.
    return results

def apply_br18_occupancy(
    spaces_with_chairs: List[Dict[str, Any]],
    *,
    br18_fallback: Callable[[Dict[str, Any]], int],
    verbose: bool = True,
) -> List[Dict[str, Any]]:
    """
    Take the output of count_chairs_by_space and assign a final occupant count
    per space.

    Logic:
      - If chair_count > 0:
            occupants = chair_count
            source = "chairs"
      - If chair_count == 0:
            occupants = br18_fallback(space_entry)
            source = "BR18_fallback"

    Parameters
    ----------
    spaces_with_chairs : list[dict]
        Output from count_chairs_by_space(...).
    br18_fallback : callable
        A function you provide that takes a single space entry (dict)
        and returns an integer default occupant count based on BR18 rules.
    verbose : bool
        If True, prints a summary per space.

    Returns
    -------
    list[dict]
        Same as input, but with two extra keys per space:
        - "final_occupants": int
        - "occupant_source": "chairs" | "BR18_fallback"
    """
    results = []

    for space in spaces_with_chairs:
        chair_count = space.get("chair_count", 0)

        if chair_count > 0:
            final_occupants = chair_count
            source = "chairs"
        else:
            # Use your BR18 logic when there are no chairs
            final_occupants = br18_fallback(space)
            source = "BR18_fallback"

        # Make a shallow copy so we don't modify the original dict (optional but nice)
        entry = dict(space)
        entry["final_occupants"] = final_occupants
        entry["occupant_source"] = source

        if verbose:
            num = space.get("space_number") or "-"
            name = space.get("space_name") or "(Unnamed Space)"
            print(
                f"Space {name} [{num}]: "
                f"chairs={chair_count}, final_occupants={final_occupants} (source={source})"
            )

        results.append(entry)

    return results

ANNEX_C_OCCUPANT_DENSITY = {
    # --- COMMERCIAL / PUBLIC BUILDINGS ---
    "office_landscaped": 17.0,                # m²/person
    "office_single": 10.0,
    "meeting_room": 2.0,
    "department_store": 17.0,

    # --- EDUCATIONAL BUILDINGS ---
    "classroom": 5.4,
    "kindergarten": 3.8,

    # --- RESIDENTIAL ---
    "detached_house": 42.5,
    "residential_apartment_retired": 28.3}

def guess_annex_c_category(space_entry: Dict[str, Any]) -> Optional[str]:
    """
    Try to guess the ANNEX_C_OCCUPANT_DENSITY key for a space
    based on its name and area.

    Returns the ANNEX C key (e.g. "office_single") or None if no match.
    """
    name = (space_entry.get("space_name") or "").lower()
    area = space_entry.get("area")  # you attach this in main.py
    if area is None:
        area = 0.0

    # --- OFFICES ---
    # If "office" / "kontor" in name:
    #   - large office (>= 16 m²) → office_landscaped
    #   - smaller office (< 16 m²) → office_single
    if "office" in name or "kontor" in name:
        if area >= 16.0:
            return "office_landscaped"
        else:
            return "office_single"

    # --- MEETING ROOMS ---
    if any(word in name for word in ["meeting", "møde", "conference", "konference", "boardroom"]):
        return "meeting_room"

    # --- DEPARTMENT STORE / SHOPS ---
    if any(word in name for word in ["store", "shop", "butik", "supermarket", "varehus"]):
        return "department_store"

    # --- CLASSROOMS ---
    if any(word in name for word in ["classroom", "class", "klasserum", "undervisning"]):
        return "classroom"

    # --- KINDERGARTEN / DAYCARE ---
    if any(word in name for word in ["kindergarten", "børnehave", "nursery", "vuggestue"]):
        return "kindergarten"

    # --- DETACHED HOUSES ---
    if any(word in name for word in ["house", "villa", "single-family"]):
        return "detached_house"

    # --- RESIDENTIAL APARTMENT (RETIRED / ELDERLY) ---
    if any(word in name for word in ["retired", "senior", "elderly", "ældre", "pleje"]):
        return "residential_apartment_retired"

    # If nothing matched, no Annex C category
    return None
