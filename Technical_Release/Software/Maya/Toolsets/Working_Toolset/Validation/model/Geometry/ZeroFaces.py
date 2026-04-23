# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Maya 2026+ (Python 3)
    23/4/2026
"""
import maya.cmds as cmds
import maya.api.OpenMaya as om

name = 'Zero Face'
check = 1
fixAble = 0

THRESHOLD = 1e-8  # nhỏ hơn nữa nếu cần


def run(nodes, selectionMesh):
    print('Running ' + __name__)

    zero_faces = []

    selList = om.MSelectionList()

    for node in nodes:
        try:
            selList.clear()
            selList.add(node)
            dagPath = selList.getDagPath(0)

            # ensure shape
            if dagPath.apiType() == om.MFn.kTransform:
                dagPath.extendToShape()

            meshFn = om.MFnMesh(dagPath)
            faceIt = om.MItMeshPolygon(dagPath)

            while not faceIt.isDone():
                area = faceIt.getArea()

                if area < THRESHOLD:
                    face_name = f"{dagPath.fullPathName()}.f[{faceIt.index()}]"
                    zero_faces.append(face_name)

                faceIt.next()

        except Exception as e:
            print(f"Error processing {node}: {e}")

    return zero_faces


def fix(*args):
    print('Fixing...')
    # Có thể auto delete hoặc merge
    return 1


def doc(*args):
    return (
        'Zero Face:\n'
        '- Face co dien tich ~ 0 (degenerate)\n'
        '- Gay loi shading, normal, export\n\n'
        'Fix:\n'
        '- Merge vertex\n'
        '- Collapse edge\n'
        '- Delete face'
    )


def report(*args):
    return 1