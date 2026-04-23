# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    23/4/2026
    Optimized for Maya 2026 (Python 3)

    Notes: Check Color Set
"""

import maya.cmds as cmds

name = 'Obj have ColorSet'
check = 1
fixAble = 1


def run(nodes=None, selectionMesh=None):
    """
    Trả về danh sách object có Color Set
    """
    print(f'Running {__name__}')

    if not nodes:
        return []

    result = []

    for node in nodes:
        # Query color sets (None nếu không có)
        color_sets = cmds.polyColorSet(node, query=True, allColorSets=True)

        if color_sets:
            result.append(node)

    return result


def fix(*args):
    """
    Mở Color Set Editor để user tự xử lý
    """
    print('Opening Color Set Editor...')
    cmds.ColorSetEditor()  # thay vì mel.eval
    return 1


def doc(*args):
    return (
        'ColorSet:\n'
        '- Object có Color Set\n\n'
        'Triệu chứng:\n'
        '- Object hiển thị màu đen / màu lạ\n\n'
        'HowToFix:\n'
        '- Mở Color Set Editor\n'
        '- Xóa Color Set không cần thiết\n'
        '- Hoặc dùng tool Master CleanUp'
    )


def report(*args):
    return 1



