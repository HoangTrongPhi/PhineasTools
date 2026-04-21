# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    22/4/2026
    Maya 2026+ (Python 3)
"""

import maya.cmds as cmds
import maya.mel as mel

name = 'Mesh Instance'
check = 1
fixAble = 1


# =========================
# CORE
# =========================
def _get_all_mesh_shapes():
    """Lấy tất cả mesh shape hợp lệ (không intermediate)"""
    return cmds.ls(type='mesh', noIntermediate=True, long=True) or []


def _is_instance(mesh):
    """Kiểm tra mesh có phải instance không"""
    parents = cmds.listRelatives(mesh, allParents=True, fullPath=True) or []
    return len(parents) > 1


def _get_instance_meshes(meshes):
    """Filter danh sách mesh instance"""
    return [m for m in meshes if _is_instance(m)]


# =========================
# MAIN API
# =========================
def run(nodes=None, selectionMesh=None):
    """
    Trả về danh sách mesh shape đang là instance
    """
    print(f'Checking: {name}')

    meshes = _get_all_mesh_shapes()
    if not meshes:
        return []

    err = _get_instance_meshes(meshes)

    # unique + stable order
    return list(dict.fromkeys(err))


def fix(err_nodes):
    """
    Convert instance mesh thành object độc lập
    """
    if not err_nodes:
        return 0

    # Lấy transform từ shape (unique luôn)
    transforms = list({
        p for m in err_nodes
        for p in (cmds.listRelatives(m, parent=True, fullPath=True) or [])
    })

    if not transforms:
        return 0

    # Save selection
    curr_sel = cmds.ls(selection=True, long=True) or []

    try:
        cmds.select(transforms, replace=True)

        # MEL nhanh hơn cmds cho case này
        mel.eval('ConvertInstanceToObject')

    except Exception as e:
        cmds.warning(f'[Mesh Instance Fix] Failed: {e}')
        return 0

    finally:
        # Restore selection an toàn
        valid_sel = [obj for obj in curr_sel if cmds.objExists(obj)]
        cmds.select(valid_sel, replace=True) if valid_sel else cmds.select(clear=True)

    print('Convert instance mesh: Done')
    return 1


# =========================
# UI / REPORT
# =========================
def notification():
    return 'Convert instance mesh Done'


def doc(*arg):
    return (
        "Mesh Instance:\n"
        "- Phát hiện các mesh đang ở dạng instance (shared shape).\n\n"
        "Fix:\n"
        "- Convert thành mesh độc lập.\n\n"
        "Manual:\n"
        "- Modify > Convert > Instance to Object"
    )


def report(*arg):
    return 1