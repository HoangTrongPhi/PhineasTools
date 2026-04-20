"""
    Hoang Trọng Phi
    16/6/2025 Đã chỉnh lại một số bug
"""

import os
import importlib
import maya.mel as mel
import maya.cmds as cmds
import getpass

# Import các module tùy chỉnh (Giả định các module này đã tồn tại trong script path)
import Common.Python.CommonPyFunction as CommonPyFunction
import Common.CommonHelpers as CommonHelpers

importlib.reload(CommonPyFunction)
importlib.reload(CommonHelpers)

#adminList = ['Phineas', 'trong', 'HuangFei']
username = getpass.getuser()
mainPath = 'C:/tempMaya/ExportFBX/'
pathSharing = 'C:/tempMaya/ExportFBX/Share/'

# Kiểm tra và tạo folder mặc định
if not os.path.exists(pathSharing):
    try:
        os.makedirs(pathSharing)
    except:
        pathSharing = mainPath  # Fallback nếu không tạo được


def ExportFBXOption(filename, FBXversion='FBX202000', FBXASCII=True, unit='cm', selection=True):
    if not cmds.pluginInfo('fbxmaya', query=True, loaded=True):
        try:
            cmds.loadPlugin('fbxmaya', quiet=True)
        except:
            cmds.confirmDialog(message="Không thể load plugin FBX.")
            return

    # Thiết lập thông số FBX
    mel.eval('FBXExportSmoothingGroups -v true;')
    mel.eval('FBXExportHardEdges -v false;')
    mel.eval('FBXExportTangents -v true;')
    mel.eval('FBXExportSmoothMesh -v false;')
    mel.eval('FBXExportInstances -v false;')
    mel.eval('FBXExportReferencedAssetsContent -v false;')
    mel.eval('FBXExportAnimationOnly -v false;')
    mel.eval('FBXExportBakeComplexAnimation -v false;')
    mel.eval('FBXExportConstraints -v false;')
    mel.eval('FBXExportSkins -v false;')
    mel.eval('FBXExportCameras -v false;')
    mel.eval('FBXExportLights -v false;')
    mel.eval('FBXExportEmbeddedTextures -v false;')
    mel.eval(f'FBXExportConvertUnitString {unit};')
    mel.eval(f'FBXExportFileVersion {FBXversion};')
    mel.eval(f'FBXExportInAscii -v {"true" if FBXASCII else "false"};')
    mel.eval('FBXExportUpAxis "y";')
    mel.eval('FBXExportGenerateLog -v false;')

    if selection:
        mel.eval(f'FBXExport -f "{filename}" -s;')
    else:
        mel.eval(f'FBXExport -f "{filename}";')

    print(f"Export thành công: {filename}")


def exportFBX():
    if cmds.ls(sl=True):
        name = f'{username}_Maya.fbx'
        fbxPath = os.path.join(mainPath, name)
        CommonPyFunction.Make_dir(mainPath)
        ExportFBXOption(fbxPath)
    else:
        cmds.warning("Chưa chọn object để export!")


def exportFBXSharing():
    if cmds.ls(sl=True):
        name = f'{username}_working.fbx'
        fbxPath = os.path.join(pathSharing, name)
        CommonPyFunction.Make_dir(pathSharing)
        ExportFBXOption(fbxPath)
    else:
        cmds.warning("Chưa chọn object để share!")


def exportFBXFolderScene(suffix='', FBXversion='FBX202000', FBXASCII=True, unit='cm', folderExport='', selection=False,
                         name=''):
    scenePath = CommonHelpers.GetScenePath()
    sceneName = CommonHelpers.GetSceneName()

    if CommonHelpers.CheckValidScene():
        currSel = cmds.ls(selection=True, long=True)

        # SỬA LỖI: Khởi tạo tempfolderExport trước
        tempfolderExport = folderExport if folderExport != '' else scenePath
        if folderExport != '':
            CommonPyFunction.Make_dir(tempfolderExport)

        finalName = name if name != '' else sceneName
        suffix_str = f'_{suffix}' if suffix != '' else ''
        fbxPath = f"{tempfolderExport}/{finalName}{suffix_str}.fbx"

        ExportFBXOption(fbxPath, FBXversion, FBXASCII, unit, selection)

        if currSel: cmds.select(currSel)
        if os.path.exists(tempfolderExport):
            os.startfile(tempfolderExport)
    return 1


def importFBXOption(filename, unlockNormals=True):
    mel.eval('FBXImportMode -v add;')
    mel.eval('FBXImportHardEdges -v false;')
    mel.eval('FBXImportUpAxis "y";')
    mel.eval('FBXImportConvertUnitString "cm";')
    mel.eval(f'FBXImportUnlockNormals -v {"true" if unlockNormals else "false"};')
    mel.eval('FBXImportShowUI -v false;')
    mel.eval(f'FBXImport -file "{filename}";')



