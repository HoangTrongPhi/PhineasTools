# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)

    note : UV nằm trong vùng hợp lệ
"""

import maya.api.OpenMaya as om

name = 'UV OutRange (0,1)'
check = 1
fixAble = 0

# CONFIG
STRICT_MODE = True  # True = chỉ cho phép 0–1, False = cho phép UDIM


# =========================
# CORE
# =========================
def _is_mesh(dag):
    return dag.apiType() == om.MFn.kMesh


# =========================
# CHECK
# =========================
def run(nodes, selectionMesh):
    print(f'Running {__name__}')

    err = []
    sel_it = om.MItSelectionList(selectionMesh)

    while not sel_it.isDone():
        dag = sel_it.getDagPath()

        # Ensure shape
        if dag.apiType() != om.MFn.kMesh:
            try:
                dag.extendToShape()
            except:
                sel_it.next()
                continue

        if not _is_mesh(dag):
            sel_it.next()
            continue

        mesh_name = dag.fullPathName()
        face_it = om.MItMeshPolygon(dag)

        while not face_it.isDone():
            if not face_it.hasUVs():
                face_it.next()
                continue

            try:
                u_array, v_array = face_it.getUVs()
            except:
                face_it.next()
                continue

            out_of_range = False

            for u, v in zip(u_array, v_array):

                # STRICT: phải nằm trong 0–1
                if STRICT_MODE:
                    if u < 0 or u > 1 or v < 0 or v > 1:
                        out_of_range = True
                        break

                # UDIM mode
                else:
                    if u < 0 or v < 0:
                        out_of_range = True
                        break

            if out_of_range:
                err.append(f"{mesh_name}.f[{face_it.index()}]")

            face_it.next()

        sel_it.next()

    return list(set(err))


# =========================
# FIX
# =========================
def fix(*args):
    print('UV Out of Range cannot be auto-fixed safely.')
    return 1


# =========================
# DOC / REPORT
# =========================
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