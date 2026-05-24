# Blender_ValidationTool/Config.py
#
# Single source of truth for all validation checks.
# To add a new check:
#   1. Add (key, label) to CHECKS in the correct category.
#   2. Implement a check function in Model/... with signature: func(obj) -> list | None
#      (return a list of problems, or empty/None if clean)
#   3. Map the key to that function in CHECK_FUNCTIONS.
# UI, Properties, RunAll, RunSingle, Refresh will all pick it up automatically.

import importlib

# ---- Model imports for dispatch table ----
from .Model.Geometry import Concave



# ---- Check catalog ----
# Structure: [ (category_title, [ (prop_key, display_label), ... ]) , ... ]
CHECKS = [
    ("Geometry", [
        ("geo_concave",     "Concave Faces"),
        ("geo_lamina",      "Lamina Faces"),
#        ("geo_nonmanifold", "Non Manifold"),
#        ("geo_zeroedge",    "Zero Edge"),
    ]),
    ("UV", [
#        ("uv_missing",  "Missing UV"),
        ("uv_multi",    "Multiple UV Sets"),
        ("uv_overlap",  "Overlap UV"),
#        ("uv_inverted", "Inverted UV"),
        ("uv_out",      "UV Out of Range"),
        ("uv_setname",  "UV Set Name"),
    ]),
    ("Texture", [
#        ("tex_missing",  "Missing Textures"),
        ("tex_invalid",  "Invalid Texture Path"),
        ("tex_unused",   "Unused Materials"),
        ("tex_colorset", "Color Set"),
    ]),
    ("Scene", [
#        ("scn_empty",   "Empty Transform"),
        ("scn_hidden",  "Hidden Objects"),
        ("scn_frozen",  "Frozen Transform"),
        ("scn_history", "History"),
    ]),
    ("Naming", [
#        ("name_default",    "Default Name"),
#        ("name_duplicate",  "Duplicate Name"),
        ("name_convention", "Naming Convention"),
    ]),
]


# ---- Dispatch table: prop_key -> check function ----
# Only keys mapped here will actually run. Unmapped keys are placeholders.
CHECK_FUNCTIONS = {
    "geo_concave": Concave.check_object,
    # "geo_lamina":      Lamina.check_object,
    # "geo_nonmanifold": NonManifold.check_object,
    # ...
}


# ---- Helpers ----
def iter_checks():
    """Yield (key, label) for every check, ignoring categories."""
    for _, items in CHECKS:
        for key, label in items:
            yield key, label


def all_keys():
    """Flat list of all check keys."""
    return [key for key, _ in iter_checks()]
