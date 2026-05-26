# -*- coding: utf-8 -*-
"""
Blender_ValidationTool/Model/Scene/HiddenObject.py

Check Hidden Object - module thuộc tầng Model của hệ thống validation.

Một object được coi là "hidden" khi bất kỳ flag sau bật:
    - hide_viewport : icon màn hình ở Outliner (loại khỏi depsgraph)
    - hide_get()    : eye icon trong 3D viewport (H key, per-view-layer)
    - hide_render   : icon máy ảnh (chỉ ẩn khi render)

Hidden object là rác trước export pipeline. Vì hidden object KHÔNG nằm
trong context.selected_objects được, check này luôn quét toàn scene -
không phụ thuộc vào việc user có chọn gì hay không.

Module này CHỈ detect, KHÔNG modify hide flags hay selection. Lý do:
muốn select hidden object trên Outliner thì BẮT BUỘC phải tắt
hide_viewport / hide_select (xem giải thích trong Controller/UnhideHidden.py).
Việc đó là side-effect đáng kể trên scene nên controller phải hỏi user
confirm trước, không thể tự ý làm.

API:

    check_object(obj) -> list[str] | None
        - list rỗng []          : object đang visible.
        - list các string       : các flag hide đang bật.
        - None                  : obj không hợp lệ / không phải MESH.

    check_and_highlight(objs) -> dict[str, list[str]] | None
        Pure detect - quét toàn scene, trả về dict các hidden object.
        Tham số `objs` bị bỏ qua (giữ để khớp signature các check khác).

        Returns
        -------
        dict[str, list[str]] | None
            - None                   : scene không có MESH nào.
            - {} (dict rỗng)         : tất cả MESH đều visible.
            - {obj_name: [flag,...]} : các obj hidden + flag tương ứng.
"""

import bpy


# ---------------------------------------------------------------------------
# Public entry-point (pure check, đăng ký trong Config.CHECK_FUNCTIONS)
# ---------------------------------------------------------------------------
def check_object(obj):
    """
    Pure check - không có side-effect.

    Returns
    -------
    list[str] | None
        - List các flag hide đang bật. Rỗng nghĩa là object visible.
        - None nếu obj không hợp lệ hoặc không phải MESH.
    """
    if obj is None or obj.data is None:
        return None
    if obj.type != 'MESH':
        return None

    flags = []
    if obj.hide_viewport:
        flags.append("hide_viewport")
    # hide_get() cần view_layer context; trong trường hợp hi hữu (obj
    # không thuộc view_layer hiện tại) có thể raise RuntimeError - bỏ qua.
    try:
        if obj.hide_get():
            flags.append("hide_viewport_3d")
    except RuntimeError:
        pass
    if obj.hide_render:
        flags.append("hide_render")
    return flags


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _all_scene_meshes(context):
    """Toàn bộ MESH có data trong scene hiện tại - kể cả hidden."""
    scene = context.scene
    if scene is None:
        return []
    return [
        o for o in scene.objects
        if o is not None and o.type == 'MESH' and o.data is not None
    ]


# ---------------------------------------------------------------------------
# Main workflow function
# ---------------------------------------------------------------------------
def check_and_highlight(objs=None):
    """
    Pure detect: quét toàn scene tìm hidden MESH.

    KHÔNG đụng hide flags, KHÔNG đụng selection - giữ nguyên trạng
    thái scene. Việc unhide + select hidden object để hiện trên
    Outliner do `validation.unhide_hidden` operator làm sau khi user
    confirm trong dialog Yes/No.

    Parameters
    ----------
    objs : Any
        Bị bỏ qua. Giữ tham số để khớp signature với các module check khác.

    Returns
    -------
    dict[str, list[str]] | None
        None / {} / {obj_name: ["hide_viewport", "hide_render", ...]}.
    """
    del objs  # nhấn mạnh: tham số không dùng

    # Edit Mode khoá tất cả ops object-level downstream; phải về Object Mode.
    if bpy.context.mode != 'OBJECT':
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except RuntimeError:
            pass

    candidates = _all_scene_meshes(bpy.context)
    if not candidates:
        return None

    issues = {}
    for o in candidates:
        flags = check_object(o)
        if flags:
            issues[o.name] = flags
    return issues


# ---------------------------------------------------------------------------
# Standalone debug
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    _result = check_and_highlight()
    if _result is None:
        print("[HiddenObject] Scene không có MESH nào.")
    elif not _result:
        print("[HiddenObject] Scene clean: không có hidden object.")
    else:
        print(f"[HiddenObject] {len(_result)} hidden object:")
        for name, flags in _result.items():
            print(f"  - {name}: {', '.join(flags)}")
