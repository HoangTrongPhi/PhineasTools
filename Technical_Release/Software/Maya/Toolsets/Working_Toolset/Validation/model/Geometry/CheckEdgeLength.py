# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Updated: 22/4/2026
    Maya 2026+ (Python 3)
"""

import maya.cmds as cmds
import maya.mel as mel

name = 'EdgeLength < 0.00000001'
check = 1
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Tìm các edge có độ dài cực nhỏ (gần như bằng 0)
    Return: danh sách vertex liên quan
    """
    print(f'Running {__name__}')

    if not nodes:
        return []

    # Lưu selection hiện tại
    original_selection = cmds.ls(selection=True) or []

    try:
        # Select nodes cần check
        cmds.select(nodes, r=True)

        # Cleanup để detect zero-length edges
        mel.eval(
            'polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","0","1e-05","1","0.01","0","1e-05","0","-1","0","0" }'
        )

        zero_length_edges = cmds.ls(selection=True) or []

        if not zero_length_edges:
            return []

        # Convert sang vertex
        vertices = cmds.polyListComponentConversion(
            zero_length_edges,
            fromEdge=True,
            toVertex=True
        ) or []

        # Flatten list (tránh nested list)
        vertices = cmds.ls(vertices, fl=True) or []

        return vertices

    except Exception as e:
        cmds.warning(f'[EdgeLength] Error: {e}')
        return []

    finally:
        # Restore selection
        if original_selection:
            cmds.select(original_selection, r=True)
        else:
            cmds.select(clear=True)
            cmds.selectMode(object=True)


def fix(vertices=None):
    """
    Hiện chưa auto fix (vì cần quyết định threshold + topology)
    """
    print('Fixing Edge Length... (Not Implemented)')
    return 0


def doc():
    return (
        'Edge Length:\n'
        '- Kiểm tra các edge có độ dài cực nhỏ (degenerate edges)\n\n'
        'Nguyên nhân:\n'
        '- Merge vertex lỗi\n'
        '- Import model lỗi\n'
        '- Modeling dirty topology\n\n'
        'Cách fix:\n'
        '- Merge/Weld vertex\n'
        '- Cleanup mesh\n'
        '- Dùng Merge Threshold hợp lý'
    )


def report():
    return 1