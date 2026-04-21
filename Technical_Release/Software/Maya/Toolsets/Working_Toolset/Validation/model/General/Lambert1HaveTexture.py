# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (Optimized)
    22/4/2026
    Maya 2026+ (Python 3)
"""

import maya.cmds as cmds

# =========================
# META DATA
# =========================
name = 'Lambert1 Has Textures'
check = 1
fixAble = 0


# =========================
# CORE LOGIC
# =========================
def get_lambert1_file_nodes():
    """
    Get all file nodes connected to lambert1
    """
    if not cmds.objExists('lambert1'):
        return []

    return cmds.listConnections('lambert1', type='file') or []


def has_texture_on_lambert1():
    """
    Check if lambert1 has any file texture
    """
    return bool(get_lambert1_file_nodes())


# =========================
# MAIN API (FOR CONTROLLER)
# =========================
def run(nodes=None, selectionMesh=None):
    """
    Entry point for QC system
    """
    print(f'Running {__name__}')

    file_nodes = get_lambert1_file_nodes()

    # Return list lỗi (QC system sẽ highlight)
    return file_nodes


def fix(*args):
    """
    Không auto fix vì có thể phá scene
    """
    print('Fix not supported for this check.')
    return 0


def notification():
    return 'Lambert1 check completed.'


def doc(*args):
    return (
        'Lambert1 Should Not Have Textures\n\n'
        '- Lambert1 là default material của Maya\n'
        '- Không nên gán texture vào lambert1\n'
        '- Điều này có thể gây lỗi pipeline (export/game engine)\n\n'
        '→ Hãy tạo material mới và assign lại.'
    )


def report(*args):
    """
    Return 1 nếu OK, 0 nếu fail
    """
    return 0 if has_texture_on_lambert1() else 1