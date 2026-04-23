# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    22/4/2026
    Maya 2026+ Compatible (Python 3)

    Notes: Check Mesh đang sử dụng Shader Maya mặc định (Lambert1)
"""

import maya.cmds as cmds

name = 'Mesh use "lambert1" mat'
check = 1
fixAble = 0


# ==============================
# INTERNAL HELPERS
# ==============================

def _get_shape(node):
    """Safely get shape from transform"""
    if cmds.nodeType(node) == 'transform':
        shapes = cmds.listRelatives(node, shapes=True, fullPath=True) or []
        return shapes[0] if shapes else None
    return node


def _get_shading_groups(shape):
    return cmds.listConnections(shape, type='shadingEngine') or []


def _get_materials(shading_groups):
    mats = []
    for sg in shading_groups:
        mats.extend(cmds.listConnections(sg, materials=True) or [])
    return list(set(mats))


# ==============================
# MAIN LOGIC
# ==============================

def run(nodes, selectionMesh=None):
    print(f"[QC] Running {__name__}")

    current_selection = cmds.ls(selection=True) or []
    error_nodes = set()

    for node in nodes:
        shape = _get_shape(node)
        if not shape:
            continue

        shading_groups = _get_shading_groups(shape)

        if not shading_groups:
            continue

        # Check initialShadingGroup
        if 'initialShadingGroup' in shading_groups:
            error_nodes.add(node)
            continue

        # Check lambert1 material
        materials = _get_materials(shading_groups)
        if 'lambert1' in materials:
            error_nodes.add(node)

    cmds.select(current_selection)
    return list(error_nodes)


# ==============================
# FIX / DOC / REPORT
# ==============================

def fix(*args):
    """
    Not auto-fixable because requires artist decision
    """
    return 0


def doc(*args):
    return (
        'Mesh đang sử dụng material mặc định (lambert1 hoặc initialShadingGroup).\n\n'
        'HowToFix:\n'
        '- Gán material đúng cho asset\n'
        '- Không dùng lambert1 cho asset production'
    )


def report(*args):
    return 1