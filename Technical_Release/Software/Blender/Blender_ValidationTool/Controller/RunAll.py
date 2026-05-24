# Blender_ValidationTool/Controller/RunAll.py

import bpy
# --- modules ---
from .. import Config
from ..Status import STATUS_NONE, STATUS_OK, STATUS_WARNING, STATUS_ERROR


class VALIDATION_OT_run_all(bpy.types.Operator):
    bl_idname = "validation.run_all"
    bl_label = "Run All Validation"

    def execute(self, context):
        props = context.scene.validation
        obj = context.active_object

        ran = 0
        for key, _ in Config.iter_checks():
            # Checkbox off -> skip and clear status.
            if not getattr(props, key, False):
                setattr(props, f"stt_{key}", STATUS_NONE)
                continue

            func = Config.CHECK_FUNCTIONS.get(key)
            if func is None:
                # No implementation yet — show as OK placeholder so the user
                # can see the slot exists. Replace with STATUS_NONE if you
                # prefer to hide unimplemented checks.
                setattr(props, f"stt_{key}", STATUS_OK)
                continue

            try:
                result = func(obj)
                status = STATUS_WARNING if result else STATUS_OK
            except Exception as e:
                status = STATUS_ERROR
                self.report({'ERROR'}, f"{key} failed: {e}")

            setattr(props, f"stt_{key}", status)
            ran += 1

        self.report({'INFO'}, f"Run all completed ({ran} checks)")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_run_all)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_run_all)
