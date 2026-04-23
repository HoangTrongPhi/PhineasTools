# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)

    Note: Check chồng UV
"""

import maya.cmds as cmds

name = 'UV Overlapped'
check = 1
fixAble = 0


# =========================
# CORE
# =========================
def _get_mesh_shapes(nodes):
    """Get mesh shapes from transforms"""
    shapes = cmds.listRelatives(nodes, shapes=True, fullPath=True) or []
    return cmds.ls(shapes, type='mesh') or []


def _get_faces(mesh):
    """Get all faces of mesh"""
    return cmds.ls(f"{mesh}.f[*]", fl=True) or []


def _has_uv(mesh):
    """Check if mesh has UV sets"""
    uv_sets = cmds.polyUVSet(mesh, q=True, allUVSets=True)
    return bool(uv_sets)


# =========================
# CHECK
# =========================
def run(nodes, selectionMesh):
    print(f'Running {__name__}')

    err = []
    meshes = _get_mesh_shapes(nodes)

    for mesh in meshes:
        # Skip nếu không có UV
        if not _has_uv(mesh):
            continue

        faces = _get_faces(mesh)
        if not faces:
            continue

        try:
            overlapping = cmds.polyUVOverlap(faces, oc=True) or []
        except Exception as e:
            print(f'[UV Overlap Error] {mesh}: {e}')
            continue

        if overlapping:
            err.extend(overlapping)

    return list(set(err))


# =========================
# FIX
# =========================
def fix(*args):
    print('UV Overlap cannot be auto-fixed reliably.')
    return 1


# =========================
# DOC / REPORT
# =========================
def doc(*args):
    return (
        'UV Overlapped: UV bị chồng lên nhau\n\n'
        'HowToFix:\n'
        '- Mở UV Editor\n'
        '- Layout / Unfold lại UV\n'
        '- Tránh overlap (trừ khi intentionally dùng tiling)'
    )


def report(*args):
    return 1