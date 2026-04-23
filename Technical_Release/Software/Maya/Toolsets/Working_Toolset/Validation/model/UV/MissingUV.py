# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)

    Note: Check Mesh thiếu UV
"""

import maya.api.OpenMaya as om

name = 'Faces Missing UV'
check = 1
fixAble = 0


# =========================
# CORE
# =========================
def _is_mesh(dag_path):
    """Check if dagPath is mesh"""
    return dag_path.apiType() == om.MFn.kMesh


# =========================
# CHECK
# =========================
def run(nodes, selectionMesh):
    print(f'Running {__name__}')

    missing_uvs = []
    sel_it = om.MItSelectionList(selectionMesh)

    while not sel_it.isDone():
        dag_path = sel_it.getDagPath()

        # Ensure shape
        if dag_path.apiType() != om.MFn.kMesh:
            try:
                dag_path.extendToShape()
            except:
                sel_it.next()
                continue

        if not _is_mesh(dag_path):
            sel_it.next()
            continue

        mesh_name = dag_path.fullPathName()
        face_it = om.MItMeshPolygon(dag_path)

        while not face_it.isDone():
            if not face_it.hasUVs():
                missing_uvs.append(f"{mesh_name}.f[{face_it.index()}]")
            face_it.next()

        sel_it.next()

    return missing_uvs


# =========================
# FIX
# =========================
def fix(*args):
    print('Faces Missing UV cannot be auto-fixed.')
    return 1


# =========================
# DOC / REPORT
# =========================
def doc(*args):
    return (
        'Faces Missing UV: face chưa được unwrap UV\n\n'
        'HowToFix:\n'
        '- Chọn các face bị lỗi\n'
        '- Thực hiện Unwrap UV (UV Editor / Automatic / Planar / etc.)'
    )


def report(*args):
    return 1