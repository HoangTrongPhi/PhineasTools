# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI (Optimized)
    22/4/2026
    Maya 2026+ (Python 3)
"""
import maya.cmds as cmds
import re

name = 'Suffix Number'
check = 0
fixAble = 0


def run(nodes, selectionMesh):
    print(f'Running {__name__}')

    trailing_numbers = []

    for node in nodes:
        mesh = node

        # Ensure transform
        if cmds.objectType(node) != 'transform':
            parents = cmds.listRelatives(node, parent=True, fullPath=True)
            if parents:
                mesh = parents[0]

        if not mesh:
            continue

        # Lấy short name (tránh full path)
        short_name = mesh.split('|')[-1]

        # Check suffix number (vd: mesh_01, mesh_2, mesh10)
        if re.search(r'\d+$', short_name):
            trailing_numbers.append(mesh)

    return trailing_numbers


def fix(*args):
    print('Fixing...')
    # Chưa implement vì cần quyết định rule rename
    return 1


def doc(*args):
    return (
        'Suffix Number:\n'
        '- Ten mesh co so o cuoi (vd: mesh_01, mesh_2)\n'
        '- Thuong do duplicate khong clean\n\n'
        'Nen rename de clean pipeline!'
    )


def report(*args):
    return 1
