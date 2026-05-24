# Blender_ValidationTool/Controller/RunSingle.py

import bpy

# --- modules ---
from .. import Config
from ..Status import STATUS_NONE, STATUS_OK, STATUS_WARNING, STATUS_ERROR


class VALIDATION_OT_run_single(bpy.types.Operator):
    bl_idname = "validation.run_single"
    bl_label = "Run Single"

    # The UI passes the full prop key here (e.g. "geo_concave"),
    # not just the suffix. The old code compared against "concave"
    # which never matched.
    check_name: bpy.props.StringProperty()

    def execute(self, context):
        props = context.scene.validation
        key = self.check_name

        # Sanity: key must exist in catalog.
        if key not in Config.all_keys():
            self.report({'WARNING'}, f"Unknown check: {key}")
            return {'CANCELLED'}

        # Checkbox must be enabled.
        if not getattr(props, key, False):
            self.report({'WARNING'}, f"'{key}' is not enabled")
            return {'CANCELLED'}

        func = Config.CHECK_FUNCTIONS.get(key)
        if func is None:
            self.report({'WARNING'}, f"No implementation for '{key}'")
            setattr(props, f"stt_{key}", STATUS_NONE)
            return {'CANCELLED'}

        obj = context.active_object
        try:
            result = func(obj)
        except Exception as e:
            setattr(props, f"stt_{key}", STATUS_ERROR)
            self.report({'ERROR'}, f"{key} failed: {e}")
            return {'CANCELLED'}

        if result:
            setattr(props, f"stt_{key}", STATUS_WARNING)
            self.report({'WARNING'}, f"{key}: {len(result)} issues found")
        else:
            setattr(props, f"stt_{key}", STATUS_OK)
            self.report({'INFO'}, f"{key}: clean")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_run_single)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_run_single)
