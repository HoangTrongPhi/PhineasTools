# -*- coding: utf-8 -*-
"""
    Author: HOANG TRONG PHI
    Maya 2026+ (Python 3)
    23/4/2026
"""
import maya.api.OpenMaya as om

name = 'Lamina'
check = 1
fixAble = 0


def run(nodes=None, selectionMesh=None):
    print('Running ' + __name__)

    laminaFaces = []

    #Build selectionMesh nếu chưa có
    if selectionMesh is None:
        selectionMesh = om.MSelectionList()
        for n in nodes or []:
            selectionMesh.add(n)

    selIt = om.MItSelectionList(selectionMesh)

    while not selIt.isDone():
        dagPath = selIt.getDagPath()

        if not dagPath.hasFn(om.MFn.kMesh):
            selIt.next()
            continue

        meshFn = om.MFnMesh(dagPath)
        faceIt = om.MItMeshPolygon(dagPath)

        objectName = dagPath.fullPathName()

        faceMap = {}  # key: vertex set, value: list faceIds

        while not faceIt.isDone():
            faceId = faceIt.index()
            verts = faceIt.getVertices()

            #key chuẩn: sorted tuple (hashable + nhanh)
            key = tuple(sorted(verts))

            faceMap.setdefault(key, []).append(faceId)

            faceIt.next()

        #detect lamina (duplicate face)
        for faces in faceMap.values():
            if len(faces) > 1:
                for fid in faces:
                    laminaFaces.append(f"{objectName}.f[{fid}]")

        selIt.next()

    return laminaFaces