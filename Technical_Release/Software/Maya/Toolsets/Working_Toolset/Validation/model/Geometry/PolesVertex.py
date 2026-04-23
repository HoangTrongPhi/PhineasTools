# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Optimized for Maya 2026 (Python 3)
    
"""

import maya.api.OpenMaya as om

name = 'Poles'
check = 0
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Trả về danh sách vertex có hơn 5 edges (pole)
    """
    print(f'Running {__name__}')

    if not selectionMesh:
        return []

    poles = []

    sel_iter = om.MItSelectionList(selectionMesh)

    while not sel_iter.isDone():
        dag_path = sel_iter.getDagPath()

        # Skip nếu không phải mesh
        if not dag_path.hasFn(om.MFn.kMesh):
            sel_iter.next()
            continue

        vertex_iter = om.MItMeshVertex(dag_path)
        obj_name = dag_path.fullPathName()

        while not vertex_iter.isDone():
            edge_count = vertex_iter.numConnectedEdges()

            # Pole: > 5 edges
            if edge_count > 5:
                vtx_index = vertex_iter.index()
                poles.append(f'{obj_name}.vtx[{vtx_index}]')

            vertex_iter.next()

        sel_iter.next()

    return poles


def fix(*args):
    """
    Không auto fix vì liên quan topology
    """
    print('Fixing...')
    return 1


def doc(*args):
    return (
        'Poles:\n'
        '- Vertex có nhiều hơn 5 edges\n\n'
        'HowToFix:\n'
        '- Retopology\n'
        '- Redirect edge flow\n'
        '- Hoặc bỏ qua nếu hợp lý (joint, deformation area)'
    )


def report(*args):
    return 1