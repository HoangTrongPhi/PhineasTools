# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Maya 2026+ (Python 3)
    note: UV set name Default phải là map1
"""

import maya.cmds as cmds

name = 'UVset Name'
check = 1
fixAble = 1

def _get_mesh_shapes(nodes):
    """Get all mesh shapes from given transform nodes"""
    shapes = cmds.listRelatives(nodes, shapes=True, fullPath=True) or []
    return cmds.ls(shapes, type='mesh') or []

def _get_uv_sets(mesh):
    """Safe get uv sets"""
    return cmds.polyUVSet(mesh, q=True, allUVSets=True) or []

def run(nodes, selectionMesh):
    print(f'Running {__name__}')
    err = []
    meshes = _get_mesh_shapes(nodes)
    for mesh in meshes:
        uv_sets = _get_uv_sets(mesh)
        if not uv_sets:
            continue

        # Rule: UV set đầu tiên phải là map1
        if uv_sets[0] != 'map1':
            err.append(mesh)
    return list(set(err))


def fix(*args):
    print('Fixing UVset Name...')

    curr_sel = cmds.ls(selection=True, long=True, type='transform') or []
    meshes = _get_mesh_shapes(curr_sel)

    for mesh in meshes:
        uv_sets = _get_uv_sets(mesh)

        if not uv_sets:
            continue

        # Nếu không có map1 → rename UV set đầu tiên thành map1
        if 'map1' not in uv_sets:
            try:
                cmds.polyUVSet(
                    mesh,
                    rename=True,
                    uvSet=uv_sets[0],
                    newUVSet='map1'
                )
            except Exception as e:
                print(f'[UVSet Rename Failed] {mesh}: {e}')
            continue

        # Nếu có map1 nhưng không phải first → set current UV
        if uv_sets[0] != 'map1':
            try:
                cmds.polyUVSet(mesh, currentUVSet=True, uvSet='map1')
            except Exception as e:
                print(f'[Set Current UV Failed] {mesh}: {e}')

    return 1


# =========================
# DOC / REPORT
# =========================
def doc(*args):
    return (
        'UVsets has wrong name\n'
        'UVset bị sai naming\n\n'
        'Rule:\n'
        '- UV set đầu tiên phải là "map1"\n'
        '- Nếu không có "map1" → sẽ rename UV set đầu tiên'
    )


def report(*args):
    return 1



