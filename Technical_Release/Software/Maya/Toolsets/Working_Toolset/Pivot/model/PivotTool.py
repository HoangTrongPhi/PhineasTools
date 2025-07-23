"""
30/10/2024
Edit by HOANG TRONG PHI   @HuangFei
Done test

10/6/2025
Da optimized code

"""
#from Qt import QtCore, QtWidgets, QtGui
import sys, os, json 
import importlib
import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

try:
    from shiboken2 import wrapInstance
    import maya.cmds as cmds, maya.mel as mel, maya.OpenMayaUI as omui, maya.api.OpenMaya as om
    print ('Import success Maya Module, shiboken2')
except:
    from shiboken6 import wrapInstance
    import maya.cmds as cmds, maya.mel as mel, maya.OpenMayaUI as omui, maya.api.OpenMaya as om
    print('Import success Maya Module, shiboken6')
else:
    pass

def getDirectoryofModule(modulename):
    """
    Input: module as string
    OUtput:
        List: name as string and directory of module
    """
    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = CommonPyFunction.Get_WD(module.__file__)
    return currWD


def getPivotPosition():
    global pivotPos
    sel = cmds.ls(sl=True)
    if len(sel) == 1 and cmds.objectType(sel) == 'transform':
        pivotPos = cmds.xform(sel, query=1, worldSpace=1, rotatePivot=1)
        print (pivotPos)
    else:
        cmds.confirmDialog(message='Phải chọn 1 mesh nào đó để Get Pivot, chỉ một mesh', title='Error')


def setPivotPosition():

    if pivotPos:
        selList = cmds.ls(selection=True)
        if selList:
            for objSel in selList:
                if cmds.objectType(objSel) == 'transform':
                    cmds.move(pivotPos[0], pivotPos[1], pivotPos[2], objSel + '.scalePivot', objSel + '.rotatePivot', absolute=True)
                if cmds.listRelatives(objSel, allDescendents=True, type='transform'):
                    for i in cmds.listRelatives(objSel, allDescendents=True, type='transform'):
                        cmds.move(pivotPos[0], pivotPos[1], pivotPos[2], i + '.scalePivot', i + '.rotatePivot', absolute=True)


def centerBottomPivot():
    """Center Bottom Pivot"""
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        bbox = cmds.exactWorldBoundingBox(obj)
        bottom = [(bbox[0] + bbox[3]) / 2, bbox[1], (bbox[2] + bbox[5]) / 2]
        cmds.xform(obj, pivots=bottom, worldSpace=True)

    return 1



def centerTopPivot():
    """Center Top Pivot"""
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        bbox = cmds.exactWorldBoundingBox(obj)
        top = [(bbox[0] + bbox[3]) / 2, bbox[4], (bbox[2] + bbox[5]) / 2]
        cmds.xform(obj, pivots=top, worldSpace=True)

    return 1


def pivotOriginal():
    sel = cmds.ls(selection=True)
    for obj in sel:
        cmds.move(0, 0, 0, obj + '.scalePivot', obj + '.rotatePivot', absolute=True)
    return 1


def centerPivot():
    mel.eval('CenterPivot')
    return 1


def setXmin():
    print ('Xmin')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [bbox[0], currPivotPos[1], currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setXmid():
    print ('Xmid')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [(bbox[0] + bbox[3]) / 2, currPivotPos[1], currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setXmax():
    print ('Xmax')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [bbox[3], currPivotPos[1], currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setYmin():
    print ('Ymin')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], bbox[1], currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setYmid():
    print ('Ymid')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], (bbox[1] + bbox[4]) / 2, currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setYmax():
    print ('Ymax')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], bbox[4], currPivotPos[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setZmin():
    print ('Zmin')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], currPivotPos[1], bbox[2]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setZmid():
    print ('Zmid')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], currPivotPos[1], (bbox[2] + bbox[5]) / 2]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1


def setZmax():
    print ('Zmax')
    currSel = cmds.ls(selection=True)
    for obj in currSel:
        currPivotPos = cmds.xform(obj, query=1, worldSpace=1, rotatePivot=1)
        bbox = cmds.exactWorldBoundingBox(obj)
        newPivotPosition = [currPivotPos[0], currPivotPos[1], bbox[5]]
        cmds.xform(obj, pivots=newPivotPosition, worldSpace=True)
    return 1

