# uncompyle6 version 3.9.1
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
# Embedded file name: G:/Technical_Dev\Maya\Toolsets\Validation_Toolset\Projects\COMMON\Naming\SuffixNumber.py
# Compiled at: 2021-06-26 21:43:23
"""
        SuffixNumber.py
    Created by otis - Nguyen Dang Khoa at 7/29/2020
    Update 11:16 AM - 29/07/2020
    
 """
import maya.cmds as cmds

name = 'Suffix Number'
check = 0
fixAble = 0

def run(nodes, selectionMesh):
    print(f'Running {__name__}')
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
    trailing_numbers = []
    for node in nodes:
        mesh = node
        if cmds.objectType(node) != 'transform':
            parents = cmds.listRelatives(node, parent=True, fullPath=True)
            if parents:
                mesh = parents[0]
        if mesh and mesh[-1] in numbers:
            trailing_numbers.append(mesh)

    return trailing_numbers


def fix(*arg):
    print('Fixing...')
    return 1


def doc(*arg):
    mess = 'Suffix Number: Ten mesh co them cac so o phia sau\nCo the do loi duplicate\n\nCo the fix hoac bo qua!'
    return mess


def report(*arg):
    return 1
