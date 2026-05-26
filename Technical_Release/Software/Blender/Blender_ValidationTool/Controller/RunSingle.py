# Blender_ValidationTool/Controller/RunSingle.py

import bpy

# --- modules ---
from .. import Config
from ..Status import STATUS_NONE, STATUS_OK, STATUS_WARNING, STATUS_ERROR
from . import UnhideHidden, ApplyHistory


class VALIDATION_OT_run_single(bpy.types.Operator):
    bl_idname = "validation.run_single"
    bl_label = "Run Single"

    # UI truyền full prop key (vd "geo_concave").
    check_name: bpy.props.StringProperty()

    def execute(self, context):
        props = context.scene.validation
        key = self.check_name

        # Sanity: key phải có trong catalog.
        if key not in Config.all_keys():
            self.report({'WARNING'}, f"Unknown check: {key}")
            return {'CANCELLED'}

        # Checkbox phải bật.
        if not getattr(props, key, False):
            self.report({'WARNING'}, f"'{key}' is not enabled")
            return {'CANCELLED'}

        # Lấy danh sách object đã được chọn.
        # - Hầu hết check chỉ chạy trên MESH -> dùng selected_meshes (đã lọc
        #   Light/Camera/Armature/...).
        # - Riêng "scn_history" còn xử lý Curve/Surface/Meta/Font (convert
        #   sang Mesh), nên cần raw selection; chính module History sẽ tự
        #   lọc lại bằng CONVERTIBLE_TYPES.
        # - Riêng "scn_hidden" KHÔNG dựa vào selection: hidden object không
        #   thể nằm trong selected_objects, nên module luôn quét toàn scene.
        #   Pass list rỗng xuống để báo "scope = scene".
        if key == "scn_history":
            meshes = [
                o for o in context.selected_objects
                if o is not None and o.type in {'MESH', 'CURVE', 'SURFACE', 'META', 'FONT'}
            ]
            require_selection = True
            warn_msg = "No convertible object selected (Light/Camera/Armature ignored)"
        elif key == "scn_hidden":
            meshes = []
            require_selection = False
            warn_msg = None
        else:
            meshes = Config.selected_meshes(context)
            require_selection = True
            warn_msg = "No mesh selected (Light/Camera/... ignored)"

        if require_selection and not meshes:
            setattr(props, f"stt_{key}", STATUS_WARNING)
            self.report({'WARNING'}, warn_msg)
            return {'CANCELLED'}

        # ---- Highlight workflow (multi-object) ưu tiên ----
        # Các check đã có highlight function nhận list và trả dict.
        highlight_func = Config.CHECK_HIGHLIGHT_FUNCTIONS.get(key)
        if highlight_func is not None:
            try:
                result = highlight_func(meshes)
            except Exception as e:
                setattr(props, f"stt_{key}", STATUS_WARNING)
                self.report({'ERROR'}, f"{key} failed: {e}")
                return {'CANCELLED'}

            if result is None:
                setattr(props, f"stt_{key}", STATUS_WARNING)
                scope = "selection" if meshes else "scene"
                self.report({'WARNING'}, f"{key}: no valid mesh in {scope}")
                return {'CANCELLED'}

            if not result:
                setattr(props, f"stt_{key}", STATUS_OK)
                scope = f"{len(meshes)} mesh" if meshes else "scene"
                self.report({'INFO'}, f"{key}: {scope} clean")
            else:
                setattr(props, f"stt_{key}", STATUS_ERROR)
                total = sum(len(v) for v in result.values())
                self.report(
                    {'WARNING'},
                    f"{key}: {total} issues across {len(result)} mesh",
                )
                # scn_hidden: hidden object không thể select qua viewport
                # API - hỏi user có muốn unhide để select trên Outliner.
                # UX: lần tick đầu chỉ báo ERROR; lần tick thứ 2+ mới mở
                # dialog confirm. State reset bởi Refresh.
                if key == "scn_hidden" and UnhideHidden.should_show_dialog():
                    bpy.ops.validation.unhide_hidden(
                        'INVOKE_DEFAULT',
                        object_names=UnhideHidden.encode_names(result.keys()),
                    )
                # scn_history: lần tick 2+ apply modifier + convert sang
                # MESH cho các obj đang lỗi. Không hỏi confirm (user yêu
                # cầu "chạy luôn"); muốn rollback dùng Ctrl+Z.
                elif key == "scn_history" and ApplyHistory.should_apply():
                    bpy.ops.validation.apply_history(
                        object_names=ApplyHistory.encode_names(result.keys()),
                    )
            return {'FINISHED'}

        # ---- Pure check fallback (no highlight) ----
        pure_func = Config.CHECK_FUNCTIONS.get(key)
        if pure_func is None:
            setattr(props, f"stt_{key}", STATUS_NONE)
            self.report({'WARNING'}, f"No implementation for '{key}'")
            return {'CANCELLED'}

        any_issue = False
        had_exception = False
        total_issues = 0
        for obj in meshes:
            try:
                result = pure_func(obj)
            except Exception as e:
                had_exception = True
                self.report({'ERROR'}, f"{key} on '{obj.name}' failed: {e}")
                continue
            if result is None:
                continue
            if result:
                any_issue = True
                total_issues += len(result)

        if had_exception:
            setattr(props, f"stt_{key}", STATUS_WARNING)
        elif any_issue:
            setattr(props, f"stt_{key}", STATUS_ERROR)
            self.report(
                {'WARNING'},
                f"{key}: {total_issues} issues across {len(meshes)} mesh",
            )
        else:
            setattr(props, f"stt_{key}", STATUS_OK)
            self.report({'INFO'}, f"{key}: {len(meshes)} mesh clean")

        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_run_single)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_run_single)
