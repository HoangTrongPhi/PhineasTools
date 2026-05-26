# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Controller/UnhideHidden.py

Operator phụ trợ cho check "scn_hidden": sau khi HiddenObject phát hiện
các object đang Hidden, RunSingle gọi operator này với INVOKE_DEFAULT
để hỏi user "có muốn hiển thị các Object đang Hidden không?".

    Yes -> tắt hide_viewport / hide_select / hide_get() trên các object
           được liệt kê, deselect all rồi select chúng (các object
           visible sẵn không bị đụng tới).
    No  -> không làm gì.

Lý do phải tách thành operator riêng (thay vì làm thẳng trong
HiddenObject.check_and_highlight):
    - Việc unhide là side-effect đáng kể trên scene; phải confirm trước.
    - invoke_confirm chỉ chạy được khi operator được INVOKE, không thể
      bật dialog từ trong Model layer.
    - Giữ Model layer pure (chỉ detect), tách UI confirmation ra
      Controller - đúng phân lớp của project.
"""

import bpy


# Object name list được truyền qua property dạng chuỗi vì Blender không
# cho phép CollectionProperty trong invoke_confirm flow đơn giản.
# Dùng newline làm separator: object name có thể chứa dấu phẩy/khoảng
# trắng nhưng không chứa newline.
_NAME_SEP = "\n"


def encode_names(names):
    """Encode list tên object thành 1 chuỗi truyền qua operator property."""
    return _NAME_SEP.join(names)


def _decode_names(blob):
    return [n for n in blob.split(_NAME_SEP) if n]


# ---------------------------------------------------------------------------
# "Warned once" flag - module-level state
# ---------------------------------------------------------------------------
# UX yêu cầu: lần tick RunSingle đầu tiên trên Hidden Objects chỉ báo
# lỗi, lần thứ 2+ mới hiện dialog confirm. Lý do: dialog popup giữa
# workflow có thể annoy user; cho họ thấy ERROR trước, nếu vẫn click
# RunSingle nghĩa là họ thật sự muốn xử lý -> mở dialog.
#
# Flag được reset khi Refresh (cùng cycle reset stt_*). Lưu module-level
# vì state này transient theo session, không cần persist vào .blend.
_already_warned = False


def should_show_dialog():
    """Quyết định lần tick này có hiện dialog hay không.

    Hành vi state machine:
        - State False (lần đầu)  -> trả False, chuyển sang True.
        - State True             -> trả True (giữ nguyên).

    Refresh sẽ gọi `reset()` để về lại False.
    """
    global _already_warned
    if _already_warned:
        return True
    _already_warned = True
    return False


def reset():
    """Refresh gọi để cycle về first-warn behavior."""
    global _already_warned
    _already_warned = False


class VALIDATION_OT_unhide_hidden(bpy.types.Operator):
    bl_idname = "validation.unhide_hidden"
    bl_label = "Show all Hidden Objects?"
    bl_description = (
        "Bật visibility và select các object đang Hidden vừa phát hiện. "
        "Các object đang hiện trên Scene được giữ nguyên."
    )
    bl_options = {'REGISTER', 'UNDO'}

    # Newline-separated list tên object cần unhide.
    object_names: bpy.props.StringProperty(
        name="Object Names",
        default="",
        options={'HIDDEN'},
    )

    # ---- Invoke: hiện dialog confirm ----
    def invoke(self, context, event):
        if not self.object_names:
            self.report({'WARNING'}, "No hidden object to show")
            return {'CANCELLED'}
        return context.window_manager.invoke_confirm(self, event)

    # ---- Execute: user chọn Yes -> unhide + select ----
    def execute(self, context):
        names = _decode_names(self.object_names)
        if not names:
            return {'CANCELLED'}

        # Ép về Object Mode trước khi đụng select_set.
        if context.mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode='OBJECT')
            except RuntimeError:
                pass

        # Deselect all - các object visible đang được user chọn cũng
        # bị bỏ chọn, nhưng visibility của chúng KHÔNG bị đụng tới
        # (yêu cầu: giữ nguyên Object đang có mặt trên Scene).
        try:
            bpy.ops.object.select_all(action='DESELECT')
        except RuntimeError:
            pass

        unhidden = []
        missing = []
        for name in names:
            obj = context.scene.objects.get(name)
            if obj is None:
                missing.append(name)
                continue

            # Tắt mọi cờ ẩn để select_set hoạt động và user nhìn thấy obj.
            # hide_render KHÔNG đụng vào - đó là render-only flag, không
            # ảnh hưởng việc thấy/select trong viewport.
            if obj.hide_viewport:
                obj.hide_viewport = False
            if obj.hide_select:
                obj.hide_select = False
            try:
                if obj.hide_get():
                    obj.hide_set(False)
            except RuntimeError:
                pass

            try:
                obj.select_set(True)
                unhidden.append(obj)
            except (RuntimeError, ReferenceError):
                # Edge case: collection của obj bị exclude khỏi view layer,
                # select_set vẫn fail dù đã tắt hide. Bỏ qua.
                pass

        if unhidden:
            try:
                context.view_layer.objects.active = unhidden[0]
            except (RuntimeError, ReferenceError):
                pass
            msg = f"Unhidden + selected {len(unhidden)} object"
            if missing:
                msg += f" ({len(missing)} not found)"
            self.report({'INFO'}, msg)
        else:
            self.report({'WARNING'}, "No object could be unhidden")
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_unhide_hidden)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_unhide_hidden)
