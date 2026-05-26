# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Controller/ApplyHistory.py

Operator phụ trợ cho check "scn_history": sau khi History phát hiện các
object còn modifier hoặc chưa phải MESH, RunSingle gọi operator này ở
lần tick thứ 2 để apply toàn bộ modifier + convert type sang MESH cho
các object đang lỗi.

Lý do tách operator riêng (không nhúng thẳng vào Model layer):
    - Apply modifier / Convert là side-effect destructive (khó undo
      nếu modifier nặng, có thể đè data linked). Phải kiểm soát chặt.
    - Giữ Model layer pure (chỉ detect), tách thao tác phá data ra
      Controller - đúng phân lớp project.

UX state machine (cùng kiểu UnhideHidden):
    - Tick 1 RunSingle "scn_history" -> báo ERROR + select các obj lỗi,
      KHÔNG apply.
    - Tick 2+ RunSingle "scn_history" -> apply ngay, không hỏi confirm
      (user yêu cầu "chạy luôn"; muốn rollback dùng Ctrl+Z).
    - Refresh reset state -> quay về Tick 1.
"""

import bpy


# Object name list được truyền qua property dạng chuỗi vì Blender không
# cho phép CollectionProperty trong operator-call đơn giản. Newline làm
# separator: object name có thể chứa dấu phẩy/khoảng trắng nhưng không
# chứa newline.
_NAME_SEP = "\n"


def encode_names(names):
    """Encode list tên object thành 1 chuỗi truyền qua operator property."""
    return _NAME_SEP.join(names)


def _decode_names(blob):
    return [n for n in blob.split(_NAME_SEP) if n]


# ---------------------------------------------------------------------------
# "Warned once" flag - module-level state
# ---------------------------------------------------------------------------
# UX: lần tick đầu chỉ báo ERROR + select, lần 2+ mới apply. Lý do:
# Apply modifier là destructive; cho user thấy danh sách obj lỗi trước,
# nếu vẫn click RunSingle nghĩa là họ thật sự muốn xử lý -> apply.
#
# Flag reset bởi Refresh. Module-level vì state transient theo session,
# không cần persist vào .blend.
_already_warned = False


def should_apply():
    """Quyết định lần tick này có apply ngay hay không.

    Hành vi state machine:
        - State False (lần đầu) -> trả False, chuyển sang True.
        - State True            -> trả True (giữ nguyên).

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


class VALIDATION_OT_apply_history(bpy.types.Operator):
    bl_idname = "validation.apply_history"
    bl_label = "Apply Modifiers / Convert to Mesh"
    bl_description = (
        "Apply tất cả modifier và convert non-MESH (Curve/Surface/Meta/Font) "
        "sang MESH cho các object đang còn history."
    )
    bl_options = {'REGISTER', 'UNDO'}

    # Newline-separated list tên object cần xử lý.
    object_names: bpy.props.StringProperty(
        name="Object Names",
        default="",
        options={'HIDDEN'},
    )

    def execute(self, context):
        names = _decode_names(self.object_names)
        if not names:
            return {'CANCELLED'}

        # Ép về Object Mode trước khi đụng select_set / modifier_apply.
        if context.mode != 'OBJECT':
            try:
                bpy.ops.object.mode_set(mode='OBJECT')
            except RuntimeError:
                pass

        applied_objects = 0     # số object xử lý xong, không có lỗi modifier
        modifier_count = 0      # tổng số modifier đã apply
        converted_count = 0     # số object được convert sang MESH
        failed = []             # list (tag, reason) khi gặp lỗi

        for name in names:
            obj = context.scene.objects.get(name)
            if obj is None:
                failed.append((name, "not found"))
                continue
            if obj.data is None:
                failed.append((name, "no data"))
                continue

            # Cô lập obj: deselect all, select riêng obj này + set active.
            # bpy.ops.object.* tác động theo active/selection nên phải
            # gom về 1 object trước khi gọi convert / modifier_apply.
            try:
                bpy.ops.object.select_all(action='DESELECT')
            except RuntimeError:
                pass
            try:
                obj.select_set(True)
                context.view_layer.objects.active = obj
            except (RuntimeError, ReferenceError) as e:
                failed.append((name, f"select failed: {e}"))
                continue

            # Non-MESH -> convert(target='MESH'). Operator này tự apply
            # mọi modifier trong lúc chuyển type cho Curve/Surface/Meta/
            # Font, nên không cần modifier_apply riêng cho nhánh này.
            if obj.type != 'MESH':
                try:
                    bpy.ops.object.convert(target='MESH')
                    converted_count += 1
                    applied_objects += 1
                except RuntimeError as e:
                    failed.append((name, f"convert failed: {e}"))
                continue

            # Đã là MESH -> apply từng modifier theo thứ tự đăng ký.
            # Snapshot tên modifier trước khi loop vì list bị mutate sau
            # mỗi apply. Linked / multi-user data sẽ raise RuntimeError;
            # bắt exception per-modifier để 1 modifier hỏng không kéo
            # theo các modifier sau bị bỏ.
            mod_names = [m.name for m in obj.modifiers]
            obj_failed = False
            for mod_name in mod_names:
                try:
                    bpy.ops.object.modifier_apply(modifier=mod_name)
                    modifier_count += 1
                except RuntimeError as e:
                    failed.append((f"{name}.{mod_name}", str(e)))
                    obj_failed = True
            if not obj_failed:
                applied_objects += 1

        # Re-select toàn bộ object vừa xử lý để user nhìn thấy scope đã
        # đụng tới (kể cả những obj failed - vẫn cần highlight để check).
        try:
            bpy.ops.object.select_all(action='DESELECT')
        except RuntimeError:
            pass
        last_active = None
        for name in names:
            obj = context.scene.objects.get(name)
            if obj is None:
                continue
            try:
                obj.select_set(True)
                last_active = obj
            except (RuntimeError, ReferenceError):
                pass
        if last_active is not None:
            try:
                context.view_layer.objects.active = last_active
            except (RuntimeError, ReferenceError):
                pass

        if failed:
            self.report(
                {'WARNING'},
                f"Applied {modifier_count} modifier(s), "
                f"converted {converted_count} object(s); "
                f"{len(failed)} item(s) failed (see console)",
            )
            for tag, reason in failed:
                print(f"[ApplyHistory] {tag}: {reason}")
        else:
            self.report(
                {'INFO'},
                f"Applied {modifier_count} modifier(s), "
                f"converted {converted_count} object(s) "
                f"on {applied_objects} target(s)",
            )
        return {'FINISHED'}


def register():
    bpy.utils.register_class(VALIDATION_OT_apply_history)


def unregister():
    bpy.utils.unregister_class(VALIDATION_OT_apply_history)
