"""
    3/11/2024
    Edit by HOANG TRONG PHI   @HuangFei
    Try to test storeTransform, restoreTransform later
"""
import maya.cmds as cmds
import sys, os
import maya.OpenMayaUI as omui
import maya.api.OpenMaya as om

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)


# Store toàn bộ SetTransform thành 1 file JSON
def storeTransform(*arg):
    import Libs.StoreSetTransform as StoreSetTransform
    importlib.reload(StoreSetTransform)
    sceneName = CommonHelpers.CheckValidScene()
    if sceneName != False:
        transformData = StoreSetTransform.StoreSetTransform()
        transformData.writeAllTransformtoJSON(sceneName)
    print('Transform stored successfully')
    return 1


# Restore tất cả transform
def restoreTransform(*arg):
    import Libs.StoreSetTransform as StoreSetTransform
    importlib.reload(StoreSetTransform)
    sceneName = CommonHelpers.CheckValidScene()
    if sceneName != False:
        transformData = StoreSetTransform.StoreSetTransform()
        transformData.applyTransform(sceneName)
    print('Restore transform successfully')


