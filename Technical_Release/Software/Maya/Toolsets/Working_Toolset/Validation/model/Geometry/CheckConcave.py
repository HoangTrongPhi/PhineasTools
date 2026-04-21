# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Maya 2026+ (Python 3)
    23/4/2026
"""

import maya.cmds as cmds
import maya.mel as mel

name = 'Concave'
check = 1
fixAble = 0


def run(nodes=None, selectionMesh=None):
    """
    Detect concave faces using Maya polyCleanup
    """
    print(f'Running {__name__}')

    if not nodes:
        return []

    # Save current selection
    original_selection = cmds.ls(selection=True, long=True) or []

    try:
        # Select target nodes
        cmds.select(nodes, r=True)

        # Run poly cleanup (concave faces)
        mel.eval(
            'polyCleanupArgList 4 { "0","2","1","0","0","1","0","0","0","0.001","0","0.01","0","1e-05","0","-1","0","0" }'
        )

        # Get result
        concave_faces = cmds.ls(selection=True, long=True) or []

    except Exception as e:
        print(f'[Concave] Error: {e}')
        concave_faces = []

    finally:
        # Restore selection safely
        if original_selection:
            cmds.select(original_selection, r=True)
        else:
            cmds.select(clear=True)
            cmds.selectMode(object=True)

    return concave_faces


def fix(*args):
    """
    No auto fix for concave faces (manual adjustment required)
    """
    print('Concave faces require manual fixing (adjust vertices).')
    return 1


def doc(*args):
    return (
        "Concave Faces:\n"
        "- Face bị lõm (non-convex), có thể gây lỗi shading hoặc export game engine.\n\n"
        "How To Fix:\n"
        "- Di chuyển vertex để mặt trở thành convex\n"
        "- Hoặc triangulate / retopology lại mesh"
    )


def report(*args):
    return 1