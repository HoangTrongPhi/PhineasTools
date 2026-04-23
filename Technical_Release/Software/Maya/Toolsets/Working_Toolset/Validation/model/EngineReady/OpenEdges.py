# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    23/4/2026
    Optimized for Maya 2026 (Python 3)
    Notes: Check hở cạnh
"""

import maya.api.OpenMaya as om

name = 'Open Edge'
check = 0
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Trả về danh sách các edge bị open (không đủ 2 face)
    """
    print(f'Running {__name__}')

    if not selectionMesh:
        return []

    open_edges = []

    sel_iter = om.MItSelectionList(selectionMesh)

    while not sel_iter.isDone():
        dag_path = sel_iter.getDagPath()
        mesh_fn = om.MFnMesh(dag_path)

        edge_iter = om.MItMeshEdge(dag_path)
        obj_name = dag_path.fullPathName()

        while not edge_iter.isDone():
            # Open edge: < 2 faces
            if edge_iter.numConnectedFaces() < 2:
                edge_index = edge_iter.index()
                open_edges.append(f'{obj_name}.e[{edge_index}]')

            edge_iter.next()

        sel_iter.next()

    return open_edges


def fix(*args):
    """
    Không auto fix vì cần xử lý topology thủ công
    """
    print('Fixing...')
    return 1


def doc(*args):
    return (
        'OpenEdges:\n'
        '- Kiểm tra mesh bị hở (hole)\n\n'
        'HowToFix:\n'
        '- Merge vertex\n'
        '- Fill Hole (Mesh > Fill Hole)\n'
        '- Bridge edge\n'
        '- Hoặc bỏ qua nếu intentional'
    )


def report(*args):
    return 1