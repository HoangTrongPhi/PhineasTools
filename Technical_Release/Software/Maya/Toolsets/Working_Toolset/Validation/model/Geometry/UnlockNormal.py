# -*- coding: utf-8 -*-
"""
    Author: HOÀNG TRỌNG PHI
    Date: 23/4/2026
    Optimized for Maya 2026 (Python 3)
"""

import maya.cmds as cmds

name = 'Mesh have Lock Normal'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print('Running ' + __name__)

    err = []

    for node in nodes:
        # Query tất cả vertex normal lock state 1 lần
        all_status = cmds.polyNormalPerVertex(
            node,
            query=True,
            freezeNormal=True
        )

        if not all_status:
            continue

        # Map lại index vertex
        for i, locked in enumerate(all_status):
            if locked:
                err.append(f"{node}.vtx[{i}]")
    return err


def fix(*args):
    print('Fixing...')
    return 1


def doc(*args):
    return (
        'LockNormal: Mesh co vertex bi lock normal\n\n'
        'HowToFix: Mesh Display > Unlock Normal\n'
        'Check lai Hard/Soft Edge'
    )

def report(*args):
    return 1