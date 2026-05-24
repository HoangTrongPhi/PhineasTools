# Blender_ValidationTool/Controller/Refresh.py

import bpy

# --- modules ---
from .. import Config
from ..Status import STATUS_NONE


class VALIDATION_OT_refresh(bpy.types.Operator):
    bl_idname = "validation.refresh"
    bl_label = "Refresh"

    def execute(self, context):
        props = context.scene.validation
        for key in Config.all_keys():
            setattr(props, f"stt_{key}", STATUS_NONE)
        self.report({'INFO'}, "Validation refreshed")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_refresh)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_refresh)
