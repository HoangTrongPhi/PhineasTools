# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Maya 2026+ (Python 3)
    Updated: 23/4/2026
"""
import maya.cmds as cmds, maya.mel as mel, maya.api.OpenMaya as om

name = 'Lamina'
check = 1
fixAble = 0

def run(nodes, selectionMesh):
    print('Running ' + __name__)
    if not nodes:
        return []
    currSel = cmds.ls(selection=True) or []
    cmds.select(nodes)
    mel.eval('polyCleanupArgList 4 { "0","2","1","0","0","0","0","0","0","0.001","0","0.01","0","1e-05","0","-1","1","0" }')
    laminaFaceList = cmds.ls(selection=True) or []
    #restore selection để tránh side-effect
    cmds.select(currSel)
    return laminaFaceList

# --------------------------------------------------
# Core Logic
# --------------------------------------------------

def _get_lamina_faces(dagPath):
    """
    Detect lamina faces on a single mesh
    """
    faceIt = om.MItMeshPolygon(dagPath)
    # map: vertex tuple -> face indices
    face_map = {}
    lamina = set()
    while not faceIt.isDone():
        face_id = faceIt.index()
        verts = faceIt.getVertices()
        key = tuple(sorted(verts))  # normalize order
        if key in face_map:
            # Found overlap → lamina
            lamina.add(face_id)
            lamina.add(face_map[key])
        else:
            face_map[key] = face_id
        faceIt.next()
    return list(lamina)


# --------------------------------------------------
# Utils
# --------------------------------------------------

def _build_selection(nodes):
    """
    Convert node list → MSelectionList
    """
    sel = om.MSelectionList()
    if not nodes:
        return sel
    for n in nodes:
        try:
            sel.add(n)
        except:
            pass
    return sel


def doc():
    return (
        'Lamina Faces:\n'
        '- Các mặt (faces) có chung cạnh, face trùng.\n\n'
        'Cách fix:\n'
        '- Delete những face bị trùng'
    )


def report():
    return 1