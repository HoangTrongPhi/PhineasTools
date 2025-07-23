"""
Author: Hoang Trong Phi -@HuangFei
Update 3/11/2024
Update 6/13/2025

"""
import maya.cmds as cmds
import maya.mel as mel

def SceneSetup():
    # maya 2026 hoạt động tốt
    cameraList = cmds.ls(type='camera')
    for cam in cameraList:
        cmds.setAttr('%s.nearClipPlane' % cam, 0.1)
        cmds.setAttr('%s.farClipPlane' % cam, 1000000.0)

    # maya2026 vẫn còn hỗ trợ
    if cmds.currentCtx() == 'selectSuperContext':
        cmds.polyOptions(gl=True, softEdge=True, sizeBorder=3, displayBorder=True, displayMapBorder=False, displayCreaseEdge=False, displayVertex=False, displayNormal=False, facet=True, displayCenter=False, displayTriangle=False, displayWarp=False, displayItemNumbers=[False, False, False, False], sizeNormal=0.4, backCulling=True, displayUVs=False, displayUVTopology=False, colorShadedDisplay=False, colorMaterialChannel='diffuse', materialBlend='overwrite', backCullVertex=False)

    panelList = cmds.getPanel(type='modelPanel')
    for panel in panelList:
        cmds.modelEditor(panel, edit=True, backfaceCulling=True)
        cmds.modelEditor(panel, edit=True, sortTransparent=True)
        cmds.modelEditor(panel, edit=True, transparencyAlgorithm='perPolygonSort')

    # maya2026 vẫn hoạt động
    cmds.optionVar(floatValue=['polyMergeVertexDistance', 0.0001])
    cmds.optionVar(floatValue=['polyMergeVertexAlwaysMergeTwoVertices', 1])
    cmds.setAttr('defaultResolution.width', 1280)
    cmds.setAttr('defaultResolution.height', 720)

    # maya2026 vẫn hoạt động
    if cmds.upAxis(q=True, axis=True) != 'y':
        cmds.upAxis(axis='y', rotateView=True)
    if not cmds.viewManip(q=True, v=True):
        cmds.viewManip(v=True)
    cmds.grid(reset=True)
    cmds.grid(size=100, sp=100, d=10)

    # chỉ khởi tạo khi nó đang mở
    if cmds.modelPanel('modelPanel4', exists=True):
        cmds.modelEditor('modelPanel4', e=True, alo=True)
        cmds.modelEditor('modelPanel4', e=True, polymeshes=True)
        cmds.modelEditor('modelPanel4', e=True, imagePlane=True)
        cmds.modelEditor('modelPanel4', e=True, cameras=True)
    try:
        cmds.playbackOptions(minTime='0sec', maxTime='1sec', animationStartTime='0sec', animationEndTime='1sec')
        mel.eval('currentTime 0 ;')
    except:
        pass
    print("Scene Setup Successful")

