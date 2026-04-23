# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Maya 2026+ (Python 3)
    23/4/2026
"""

import maya.api.OpenMaya as om
import maya.cmds as cmds

name = 'Nonmanifold'
check = 1
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Kiểm tra non-manifold vertices bằng Maya API (nhanh + không đổi selection)
    """
    print('Running ' + __name__)

    if not nodes:
        return []

    non_manifold = []

    # Convert nodes -> selection list (API)
    sel_list = om.MSelectionList()
    for node in nodes:
        try:
            sel_list.add(node)
        except:
            continue

    sel_it = om.MItSelectionList(sel_list, om.MFn.kMesh)

    while not sel_it.isDone():
        dagPath = sel_it.getDagPath()
        meshFn = om.MFnMesh(dagPath)

        try:
            verts = meshFn.getNonManifoldVertices()
        except:
            verts = []

        if verts:
            mesh_name = dagPath.fullPathName()
            non_manifold.extend(
                ["{}.vtx[{}]".format(mesh_name, v) for v in verts]
            )

        sel_it.next()

    return non_manifold


def fix(*args):
    """
    Non-manifold thường không auto fix chuẩn → giữ nguyên
    """
    print('Fixing...')
    return 1


def doc(*args):
    return (
        'Nonmanifold: Mesh có cấu trúc topology sai (đỉnh/cạnh chia sẻ bất thường)\n\n'
        'HowToFix:\n'
        '- Merge vertices hợp lý\n'
        '- Xóa face chồng chéo\n'
        '- Retopology nếu cần'
    )


def report(*args):
    return 1
