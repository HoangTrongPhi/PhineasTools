# Blender_ValidationTool/Config.py
#
# Single source of truth for all validation checks.
# To add a new check:
#   1. Add (key, label) to CHECKS in the correct category.
#   2. Implement a check function in Model/... with signature: func(obj) -> list | None
#      (return a list of problems, or empty/None if clean)
#   3. Map the key to that function in CHECK_FUNCTIONS.
# UI, Properties, RunAll, RunSingle, Refresh will all pick it up automatically.

# ---- Model imports for dispatch table ----
from .Model.Geometry import Concave, LaminaFaces, OverlapVertex
from .Model.UV import Multi_UVset, OverlapUV
from .Model.Scene import History, FrozenTransform, HiddenObject

# ---- Check catalog ----
# Structure: [ (category_title, [ (prop_key, display_label), ... ]) , ... ]
CHECKS = [
    ("Geometry", [
        ("geo_concave",     "Concave Faces"),
        ("geo_lamina",      "Lamina Faces"),
        ("geo_overlapvertex","Overlap Vertex"),
#        ("geo_nonmanifold", "Non Manifold"),
#        ("geo_zeroedge",    "Zero Edge"),
    ]),
    ("UV", [
#        ("uv_missing",  "Missing UV"),
        ("uv_multi",    "Multiple UV Sets"),
        ("uv_overlap",  "Overlap UV"),
#        ("uv_inverted", "Inverted UV"),
#        ("uv_out",      "UV Out of Range"),
#        ("uv_setname",  "UV Set Name"),
    ]),
    ("Texture", [
#        ("tex_missing",  "Missing Textures"),
        ("tex_invalid",  "Invalid Texture Path"),
        ("tex_unused",   "Unused Materials"),
#        ("tex_colorset", "Color Set"),
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
# Dùng cho RunAll / batch / report. Không side-effect lên viewport.
CHECK_FUNCTIONS = {
    "geo_concave": Concave.check_object,
    "geo_lamina": LaminaFaces.check_object,
    "geo_overlapvertex": OverlapVertex.check_object,

    "uv_multi": Multi_UVset.check_object,
    "uv_overlap": OverlapUV.check_object,

    "scn_history": History.check_object,
    "scn_frozen": FrozenTransform.check_object,
    "scn_hidden": HiddenObject.check_object,

    # "geo_nonmanifold": NonManifold.check_object,
    # ...
}
# ---- Dispatch table: prop_key -> highlight workflow function ----
# Dùng cho RunSingle / button "Run Check" trên UI. Có side-effect:
# vào Edit Mode, hide convex, đăng ký Tab watcher.
# Key nào không có ở đây -> fallback về CHECK_FUNCTIONS (chỉ check, không highlight).
CHECK_HIGHLIGHT_FUNCTIONS = {
    "geo_concave": Concave.check_and_highlight,
    "geo_lamina": LaminaFaces.check_and_highlight,
    "geo_overlapvertex": OverlapVertex.check_and_highlight,

    "uv_multi": Multi_UVset.check_and_highlight,
    "uv_overlap": OverlapUV.check_and_highlight,

    "scn_history": History.check_and_highlight,
    "scn_frozen": FrozenTransform.check_and_highlight,
    "scn_hidden": HiddenObject.check_and_highlight,
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

def selected_meshes(context):
    """Selected objects, lọc bỏ Light/Camera/Empty/Curve... — chỉ giữ MESH có data.

    Dùng cho mọi controller: validation pipeline chỉ thao tác mesh, các loại
    object khác bị bỏ qua một cách tường minh thay vì âm thầm trả None.
    """
    return [
        o for o in context.selected_objects
        if o is not None and o.type == 'MESH' and o.data is not None
    ]
