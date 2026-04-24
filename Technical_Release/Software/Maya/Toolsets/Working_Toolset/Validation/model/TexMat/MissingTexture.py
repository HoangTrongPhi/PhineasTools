# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI 
    22/4/2026
    Maya 2026+ (Python 3)

    Notes: Texture trong Scene bị Missing
"""

import os
import maya.cmds as cmds

name = 'Missing Textures'
check = 1
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Kiểm tra các file texture bị missing trong scene
    """
    print(f'Running {__name__}')
    err = []

    # Lấy tất cả file texture node (ổn định hơn textures=True)
    file_nodes = cmds.ls(type='file') or []
    for node in file_nodes:
        attr = f"{node}.fileTextureName"

        # Skip nếu attr không tồn tại
        if not cmds.objExists(attr):
            continue
        try:
            file_path = cmds.getAttr(attr)
        except Exception:
            continue
        # Skip nếu path rỗng
        if not file_path:
            continue
        # Normalize path (tránh lỗi slash)
        file_path = os.path.normpath(file_path)
        # Check tồn tại
        if not os.path.exists(file_path):
            err.append(node)
    # Remove duplicate (nếu có)
    return list(set(err))

def fix(*args):
    """
    Module này không auto fix được → chỉ return
    """
    print('Fix not supported for Missing Textures')
    return 1


def notification():
    return 'Missing Texture Check Done'


def doc(*args):
    return (
        'Missing Texture:\n'
        '- Texture không tìm thấy trong đường dẫn.\n\n'
        'How To Fix:\n'
        '- Kiểm tra lại path texture.\n'
        '- Đảm bảo file tồn tại trên disk.\n'
        '- Sử dụng File Path Editor trong Maya để repath.'
    )


def report(*args):
    return 1