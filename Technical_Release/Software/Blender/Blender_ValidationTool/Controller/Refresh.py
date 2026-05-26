# Blender_ValidationTool/Controller/Refresh.py

import bpy

# --- modules ---
from .. import Config
from ..Status import STATUS_NONE
from ..Model.Geometry import OverlapVertex
from . import UnhideHidden, ApplyHistory


class VALIDATION_OT_refresh(bpy.types.Operator):
    bl_idname = "validation.refresh"
    bl_label = "Refresh"

    def _force_object_mode(self, context):
        """Cố gắng đưa Blender về Object Mode kể cả khi active object bất thường."""
        if context.mode == 'OBJECT':
            return

        view_layer = context.view_layer
        active = view_layer.objects.active

        # Active object hiện tại có dùng được không?
        # (tồn tại, nằm trong view layer, và không bị ẩn)
        def _usable(obj):
            return (
                obj is not None
                and obj.name in view_layer.objects
                and obj.visible_get()
            )

        # Nếu active không dùng được, tìm 1 object khác làm active tạm thời
        if not _usable(active):
            fallback = next(
                (o for o in view_layer.objects if o.visible_get()),
                None,
            )
            if fallback is None:
                # Không có object nào để set active → chịu, bỏ qua
                return
            view_layer.objects.active = fallback

        # Thử mode_set; nếu vẫn fail thì dùng editmode_toggle như phương án 2
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            try:
                bpy.ops.object.editmode_toggle()
            except RuntimeError:
                pass  # đã cố hết sức, để nguyên

    def execute(self, context):
        # 1) Đưa Blender về Object Mode (có fallback)
        self._force_object_mode(context)

        # 2) Bỏ chọn toàn bộ object + xoá active
        if context.mode == 'OBJECT':
            try:
                bpy.ops.object.select_all(action='DESELECT')
            except RuntimeError:
                # Fallback nếu select_all không poll được vì lý do nào đó
                for obj in context.view_layer.objects:
                    obj.select_set(False)
        context.view_layer.objects.active = None

        # 3) Reset toàn bộ status về STATUS_NONE
        props = context.scene.validation
        for key in Config.all_keys():
            setattr(props, f"stt_{key}", STATUS_NONE)

        # 4) Khôi phục View3D cho các module có thay đổi viewport
        # (msgbus của OverlapVertex thường đã tự fire khi mode_set ở
        # bước 1, nhưng gọi tường minh để chắc chắn).
        OverlapVertex.restore_state()

        # 5) Reset transient state của các operator gắn liền với check.
        # scn_hidden có 2-stage prompt: lần 1 ERROR, lần 2 dialog. Refresh
        # đưa lại về lần 1.
        UnhideHidden.reset()
        # scn_history cũng 2-stage: lần 1 ERROR, lần 2 apply modifier.
        ApplyHistory.reset()

        self.report({'INFO'}, "Validation refreshed")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_refresh)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_refresh)