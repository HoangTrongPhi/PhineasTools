# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Optimized for Maya 2026 (Python 3)
    Notes: Check Pivot center
"""

import maya.cmds as cmds

name = 'Pivot at [0,0,0]'
check = 1
fixAble = 1


def run(nodes=None, selectionMesh=None):
    """
    Trả về danh sách object có pivot KHÔNG ở (0,0,0)
    """
    print(f'Running {__name__}')

    if not nodes:
        return []

    error_nodes = []

    for node in nodes:
        transform = _get_transform(node)
        if not transform:
            continue

        pivot = cmds.xform(transform, query=True, ws=True, rp=True)

        if pivot != [0.0, 0.0, 0.0]:
            error_nodes.append(node)

    return error_nodes


def fix(*args):
    """
    Move pivot về (0,0,0) cho selection hiện tại
    """
    print('Move Pivot to (0,0,0) Done')

    selection = cmds.ls(selection=True) or []

    for obj in selection:
        transform = _get_transform(obj)
        if not transform:
            continue

        cmds.move(
            0, 0, 0,
            f'{transform}.scalePivot',
            f'{transform}.rotatePivot',
            absolute=True
        )

    return 1


def doc(*args):
    return (
        'Pivot at [0,0,0]:\n'
        '- Kiểm tra pivot không nằm tại gốc world\n\n'
        'HowToFix:\n'
        '- Move pivot về (0,0,0)\n'
        '- Hoặc đặt pivot theo yêu cầu pipeline'
    )


def report(*args):
    return 1


# -------------------------
# Helper
# -------------------------
def _get_transform(node):
    """
    Trả về transform node tương ứng
    """
    if not cmds.objExists(node):
        return None

    if cmds.objectType(node) == 'transform':
        return node

    parent = cmds.listRelatives(node, parent=True, fullPath=True) or []
    return parent[0] if parent else None