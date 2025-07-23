"""
Author: Hoang Trong Phi -@HuangFei
Update 3/11/2024
Update 6/13/2025

"""
import maya.cmds as cmds, maya.mel as mel, time

def _progressBarInit(title='Master Fixed Meshes', status='Fixing', numJobs=100):
    if numJobs == 0:
        numJobs = 1
    cmds.progressWindow(title=title, st=status, progress=0, min=0, max=numJobs, isInterruptable=False)


def _doFixCorruptObject(theCube, theObjFullPath, queryTheObjUVSets):
    theObjParentList = cmds.listRelatives(theObjFullPath, parent=True, fullPath=True) or []
    if theObjParentList != []:
        theObjParent = theObjParentList[0]
    keepingPathCube = cmds.duplicate(theCube)[0]
    if theObjParentList != []:
        cmds.parent(keepingPathCube, theObjParent)
    if queryTheObjUVSets:
        theObjAllUVSets = cmds.polyUVSet(theObjFullPath, query=True, allUVSets=True) or []
        moreValidUVSets = ('map2', 'map3', 'map4', 'map5')
        for aUVSet in moreValidUVSets:
            if aUVSet in theObjAllUVSets:
                cmds.polyUVSet(theCube, create=True, uvSet=aUVSet)

    uvSetList = cmds.polyUVSet(theObjFullPath, query=True, allUVSets=True)
    if len(uvSetList) == 1:
        if uvSetList[0] != 'map1':
            cmds.polyUVSet(theObjFullPath, rename=True, newUVSet='map1')
    extraAttrDict = {}
    allExtraAttrs = cmds.listAttr(theObjFullPath, userDefined=True)
    if allExtraAttrs:
        for extraAttr in allExtraAttrs:
            attrType = cmds.getAttr(theObjFullPath + '.' + extraAttr, typ=True)
            attrValue = cmds.getAttr(theObjFullPath + '.' + extraAttr)
            extraAttrDict[extraAttr] = [attrType, attrValue]

    pivotPos = cmds.xform(theObjFullPath, q=1, ws=1, rp=1)
    newObj = cmds.polyUnite((theCube, theObjFullPath), ch=False)[0]
    for attr in extraAttrDict:
        cmds.addAttr(newObj, longName=attr, dt=extraAttrDict[attr][0])
        cmds.setAttr(newObj + '.' + attr, extraAttrDict[attr][1], type=extraAttrDict[attr][0])

    cmds.move(pivotPos[0], pivotPos[1], pivotPos[2], newObj + '.scalePivot', newObj + '.rotatePivot', absolute=True)
    cmds.delete(newObj + '.f[0:5]')
    cmds.delete(newObj, ch=True)
    theObjFullPath_Tokens = theObjFullPath.split('|')
    newObj = cmds.rename(newObj, theObjFullPath_Tokens[len(theObjFullPath_Tokens) - 1])
    print (newObj)
    if theObjParentList != []:
        cmds.parent(newObj, theObjParent)
    cmds.delete(keepingPathCube)


def fixCorruptedObjects():
    start_time = time.time()
    print ('Master Fix Meshes: .......\n')
    selection = cmds.ls(sl=True, long=True, dagObjects=True, type='transform') or []
    if len(selection) > 0:
        cmds.delete(selection, ch=True)
        theTempCube = cmds.polyCube(ch=False, w=1, h=1, d=1, cuv=4)[0]
        cmds.delete(theTempCube, ch=True)
        numJobs = len(selection)
        _progressBarInit(title='Master Fixed Meshes', status='Fixing...', numJobs=numJobs)
        progressBarIdx = 0
        for mesh in selection:
            if cmds.objExists(mesh):
                childrenShapes = cmds.listRelatives(mesh, children=True, type='mesh') or []
                if childrenShapes != []:
                    cmds.progressWindow(edit=True, status='Master Fix on: ' + mesh)
                    _doFixCorruptObject(cmds.duplicate(theTempCube)[0], mesh, False)
            progressBarIdx += 1
            cmds.progressWindow(edit=True, progress=progressBarIdx)

        cmds.progressWindow(endProgress=True)
        cmds.delete(theTempCube)
        cmds.select(selection)
    print ('Info: Fix took %s seconds !\n' % (time.time() - start_time))
    print ('Info: Master Fix Meshes: DONE\n')


def run():
    mess = 'Do you want to fix mesh?'
    confirm = cmds.confirmDialog(title='Are you sure?', message=mess, button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
    if confirm == 'Yes':
        fixCorruptedObjects()
    return 1
