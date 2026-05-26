# Blender_ValidationTool/Controller/RunAll.py

import bpy
# --- modules ---
from .. import Config
from ..Status import STATUS_NONE, STATUS_OK, STATUS_WARNING, STATUS_ERROR


class VALIDATION_OT_run_all(bpy.types.Operator):
    bl_idname = "validation.run_all"
    bl_label = "Run All"

    def execute(self, context):
        props = context.scene.validation

        # Lấy danh sách mesh trong selection. Light/Camera/Empty/Curve/...
        # bị lọc thẳng từ đây để mọi check phía sau không cần phòng thân.
        meshes = Config.selected_meshes(context)

        # Không có mesh nào -> set WARNING cho mọi check enabled và return.
        if not meshes:
            for key, _ in Config.iter_checks():
                if getattr(props, key, False):
                    setattr(props, f"stt_{key}", STATUS_WARNING)
                else:
                    setattr(props, f"stt_{key}", STATUS_NONE)
            self.report({'WARNING'}, "No mesh selected (Light/Camera/... ignored)")
            return {'CANCELLED'}

        ran = 0
        for key, _ in Config.iter_checks():
            # Checkbox off -> skip và clear status.
            if not getattr(props, key, False):
                setattr(props, f"stt_{key}", STATUS_NONE)
                continue

            func = Config.CHECK_FUNCTIONS.get(key)
            if func is None:
                # Chưa có implementation — placeholder OK để UI thấy slot tồn tại.
                setattr(props, f"stt_{key}", STATUS_OK)
                continue

            # Aggregate qua mọi mesh được chọn.
            # - any_issue:   có ít nhất 1 mesh phát hiện lỗi -> ERROR.
            # - any_skipped: có obj trả None (về lý thuyết không xảy ra vì đã
            #                lọc, nhưng giữ guard để không bao giờ set OK sai).
            # - had_exception: bất kỳ obj nào ném exception -> WARNING.
            any_issue = False
            had_exception = False
            for obj in meshes:
                try:
                    result = func(obj)
                except Exception as e:
                    had_exception = True
                    self.report({'ERROR'}, f"{key} on '{obj.name}' failed: {e}")
                    continue
                if result is None:
                    # Object không hợp lệ theo check function — coi như skip.
                    continue
                if result:
                    any_issue = True

            if had_exception:
                status = STATUS_WARNING
            elif any_issue:
                status = STATUS_ERROR
            else:
                status = STATUS_OK

            setattr(props, f"stt_{key}", status)
            ran += 1

        self.report(
            {'INFO'},
            f"Run all completed ({ran} checks on {len(meshes)} mesh)",
        )
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_run_all)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_run_all)
