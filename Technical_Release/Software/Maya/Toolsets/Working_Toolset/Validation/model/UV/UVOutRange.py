# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)

    note : UV nằm trong vùng hợp lệ
"""
# -*- coding: utf-8 -*-
"""
Module: UV Shell OutRange (0,1)
"""
import maya.api.OpenMaya as om

name = 'UV Shell OutRange (0,1)'
check = 1
fixAble = 0

STRICT_MODE = True
EPS = 1e-6  # Chống float error


def _to_selection_list(nodes):
    """
    Chuyển đổi list string sang MSelectionList để API 2.0 có thể đọc được.
    """
    sel = om.MSelectionList()
    for n in nodes or []:
        try:
            sel.add(n)
        except Exception:
            pass
    return sel

def run(nodes=None, selectionMesh=None):
    print(f'[QC] Running: {name}')
    # Đảm bảo đầu vào là MSelectionList để tránh lỗi ValueError [cite: 10, 11]
    if isinstance(selectionMesh, list):
        selectionMesh = _to_selection_list(selectionMesh)
    if not selectionMesh or selectionMesh.isEmpty():
        return []
    error_faces = set()
    sel_it = om.MItSelectionList(selectionMesh)
    while not sel_it.isDone():
        try:
            dag = sel_it.getDagPath()
        except Exception:
            sel_it.next()
            continue
        # Tìm đến Shape node
        if dag.apiType() != om.MFn.kMesh:
            try:
                dag.extendToShape()
            except Exception:
                pass
        if dag.apiType() != om.MFn.kMesh:
            sel_it.next()
            continue
        mesh_fn = om.MFnMesh(dag)
        mesh_name = dag.fullPathName()  # Dùng fullPathName để an toàn với object trùng tên [cite: 26]
        uv_sets = mesh_fn.getUVSetNames()
        if not uv_sets:
            sel_it.next()
            continue
        uv_set = mesh_fn.currentUVSetName()
        try:
            # Lấy mảng tọa độ và ID của các Shell
            u_array, v_array = mesh_fn.getUVs(uv_set)
            shell_count, shell_ids = mesh_fn.getUvShellsIds(uv_set)
        except Exception:
            sel_it.next()
            continue

        # Group UV theo shell ID
        shells = {}
        for uv_id in range(len(u_array)):
            shell_id = shell_ids[uv_id]
            shells.setdefault(shell_id, []).append(uv_id)

        bad_shells = set()

        # Kiểm tra từng UV trong các Shell
        for shell_id, uv_ids in shells.items():
            for uv_id in uv_ids:
                u = u_array[uv_id]
                v = v_array[uv_id]
                if STRICT_MODE:
                    if (u < 0.0 - EPS or u > 1.0 + EPS or
                            v < 0.0 - EPS or v > 1.0 + EPS):
                        bad_shells.add(shell_id)
                        break  # Chỉ cần 1 vertex vi phạm là bắt luôn cả shell
                else:
                    if u < 0.0 - EPS or v < 0.0 - EPS:
                        bad_shells.add(shell_id)
                        break
        if not bad_shells:
            sel_it.next()
            continue

        # --- TỐI ƯU CỰC MẠNH: Map Shell Lỗi Trở Lại Face ---
        try:
            # Lấy số lượng UV per face (uv_counts) và ID của từng UV theo thứ tự face (face_uv_ids)
            uv_counts, face_uv_ids = mesh_fn.getAssignedUVs(uv_set)
            uv_index = 0
            for face_id, count in enumerate(uv_counts):
                face_is_bad = False
                for _ in range(count):
                    uv_id = face_uv_ids[uv_index]

                    # Nếu UV này thuộc về một shell nằm trong danh sách đen
                    if not face_is_bad and shell_ids[uv_id] in bad_shells:
                        face_is_bad = True
                    uv_index += 1

                # Báo lỗi nguyên mặt đó
                if face_is_bad:
                    error_faces.add(f"{mesh_name}.f[{face_id}]")
        except Exception:
            pass
        sel_it.next()
    return list(error_faces)



def fix(*args):
    print('UV Out of Range cannot be auto-fixed safely.')
    return 1



def doc(*args):
    return (
        'UV OutRange:\n'
        '- UV nằm ngoài vùng hợp lệ\n\n'
        'Modes:\n'
        '- Strict: UV phải nằm trong 0–1\n'
        '- UDIM: cho phép >1 nhưng không cho phép <0\n\n'
        'HowToFix:\n'
        '- Mở UV Editor\n'
        '- Move UV vào vùng hợp lệ\n'
        '- Hoặc Layout lại UV'
    )


def report(*args):
    return 1