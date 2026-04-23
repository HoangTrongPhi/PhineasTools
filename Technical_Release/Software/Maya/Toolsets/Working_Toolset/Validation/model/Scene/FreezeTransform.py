# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (Optimized)
    22/4/2026
    Maya 2026+ (Python 3)

"""

import maya.cmds as cmds

name = 'Need FreezeTransform'
check = 1
fixAble = 1

# =========================
# CORE CHECK
# =========================
def run(nodes, selectionMesh=None):
    print(f'Running {__name__}')

    if not nodes:
        return []

    error_nodes = []

    for node in nodes:
        if not cmds.objExists(node):
            continue

        # luôn lấy transform
        if cmds.objectType(node) != 'transform':
            parents = cmds.listRelatives(node, parent=True, fullPath=True) or []
            if not parents:
                continue
            node = parents[0]

        try:
            # lấy 1 lần cho nhanh
            trans = cmds.xform(node, q=True, t=True, ws=False)
            rot = cmds.xform(node, q=True, ro=True, ws=False)
            scale = cmds.xform(node, q=True, s=True, r=True)

            if (
                any(abs(v) > 1e-6 for v in trans) or
                any(abs(v) > 1e-6 for v in rot) or
                any(abs(v - 1.0) > 1e-6 for v in scale)
            ):
                error_nodes.append(node)

        except Exception:
            continue

    return list(set(error_nodes))


# =========================
# FIX
# =========================
def fix(nodes=None):
    if not nodes:
        nodes = cmds.ls(selection=True) or []

    if not nodes:
        return 0

    cmds.makeIdentity(
        nodes,
        apply=True,
        translate=True,
        rotate=True,
        scale=True,
        normal=False
    )

    print('Freeze transform Done')
    return 1


# =========================
# UI TEXT
# =========================
def notification():
    return 'Freeze transform Done'


def doc():
    return (
        'Objects have non-zero transforms.\n\n'
        'Issue:\n'
        '- Translate ≠ (0,0,0)\n'
        '- Rotate ≠ (0,0,0)\n'
        '- Scale ≠ (1,1,1)\n\n'
        'How to fix:\n'
        '- Click Fix button\n'
        '- Or: Modify > Freeze Transforms'
    )


def report():
    return 1