# Blender_ValidationTool/Properties.py
#
# Builds ValidationProps dynamically from Config.CHECKS.
# For every check key K, two properties are created:
#   - K           : BoolProperty  (the checkbox)
#   - stt_K       : EnumProperty  (the status)
# No need to ever edit this file when adding a new check —
# edit Config.CHECKS instead.

import bpy

# --- modules ---
from . import Config
from .Status import STATUS_ITEMS, STATUS_NONE

def _build_annotations():
    annotations = {}
    for key, label in Config.iter_checks():
        annotations[key] = bpy.props.BoolProperty(
            name=label, default=False
        )
        annotations[f"stt_{key}"] = bpy.props.EnumProperty(
            items=STATUS_ITEMS, default=STATUS_NONE
        )
    return annotations


# Dynamically construct the PropertyGroup. Blender registers properties
# from __annotations__, so injecting them via type() works the same as
# declaring them by hand in a class body.
ValidationProps = type(
    "ValidationProps",
    (bpy.types.PropertyGroup,),
    {"__annotations__": _build_annotations()},
)


def register():
    bpy.utils.register_class(ValidationProps)
    bpy.types.Scene.validation = bpy.props.PointerProperty(type=ValidationProps)


def unregister():
    if hasattr(bpy.types.Scene, "validation"):
        del bpy.types.Scene.validation
    bpy.utils.unregister_class(ValidationProps)
