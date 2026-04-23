# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)

    Note: Check ngược mặt UV
"""

import maya.api.OpenMaya as om
import maya.cmds as cmds

name = 'Inverted UV'
check = 1
fixAble = 1


# =========================
# CORE
# =========================
def _get_mesh_shapes(nodes):
    shapes = cmds.listRelatives(nodes, shapes=True, fullPath=True) or []
    return cmds.ls(shapes, type='mesh') or []


def _get_uv_area_sign(uvs):
    """
    Tính signed area (shoelace formula)
    < 0 = inverted
    """
    area = 0.0
    for i in range(len(uvs)):
        x1, y1 = uvs[i]
        x2, y2 = uvs[(i + 1) % len(uvs)]
        area += (x1 * y2 - x2 * y1)
    return area * 0.5


# =========================
# CHECK
# =========================
def run(nodes, selectionMesh):
    print(f'Running {__name__}')

    err = []
    meshes = _get_mesh_shapes(nodes)

    for mesh in meshes:
        sel = om.MSelectionList()
        sel.add(mesh)
        dag = sel.getDagPath(0)

        face_it = om.MItMeshPolygon(dag)

        while not face_it.isDone():
            try:
                uvs = face_it.getUVs()
                uv_coords = list(zip(uvs[0], uvs[1]))

                if len(uv_coords) >= 3:
                    if _get_uv_area_sign(uv_coords) < 0:
                        err.append(f"{mesh}.f[{face_it.index()}]")

            except:
                pass

            face_it.next()

    return err


# =========================
# FIX
# =========================
def fix(*args):
    print('Fixing Inverted UV...')

    faces = cmds.ls(selection=True, fl=True) or []
    if not faces:
        return 1

    try:
        cmds.polyFlipUV(faces, flipType=0)  # 0 = flip U direction
    except Exception as e:
        print(f'[Flip UV Failed]: {e}')

    return 1


# =========================
# DOC / REPORT
# =========================
def doc(*args):
    return (
        'UV Inverted: UV bị lộn (orientation sai, thường hiển thị đỏ)\n\n'
        'HowToFix:\n'
        '- Chọn face lỗi\n'
        '- UV Editor → Flip (U hoặc V)\n'
        '- Hoặc dùng tool auto fix\n'
    )


def report(*args):
    return 1