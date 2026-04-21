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

mainPath = 'C:/tempMaya/ExportFBX/Custom'
pathSharing = 'C:/tempMaya/ExportFBX/Share/'

blenderPath = 'C:/tempMaya/ExportFBX/Blender/'
MayaPath = 'C:/tempMaya/ExportFBX/Maya/'

# engine
UnrealPath = 'C:/tempMaya/ExportFBX/Unreal/'
UnityPath = 'C:/tempMaya/ExportFBX/Unity/'

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

def fix_duplicate_names():
    all_nodes = cmds.ls(dag=True, long=True)
    short_names = {}

    for node in all_nodes:
        short = node.split("|")[-1]
        if short in short_names:
            new_name = cmds.rename(node, short + "_fix")
            print("Renamed:", node, "->", new_name)
        else:
            short_names[short] = node


def exportFBX(customPath = None):
    if cmds.ls(sl=True):
        name = f'{username}_Custom.fbx'
        if not customPath:
            return  # stop nếu không có path
        fbxPath = os.path.join(customPath, name)
        CommonPyFunction.Make_dir(customPath)
        ExportFBXOption(fbxPath)
    else:
        cmds.warning("Chưa chọn object để export!")


def exportToBlender():
    if cmds.ls(sl=True):
        name = f'{username}_Maya.fbx'
        fbxPath = os.path.join(MayaPath, name)
        CommonPyFunction.Make_dir(MayaPath)
        ExportFBXOption(fbxPath)
    else:
        cmds.warning("Chưa chọn object để export!")
        cmds.confirmDialog(title="Error",
                           message="Chưa chọn object để export!",
                           button=["Confirm Export"])


def exportFBXSharing():
    if cmds.ls(sl=True):
        name = f'{username}_working.fbx'
        fbxPath = os.path.join(pathSharing, name)
        CommonPyFunction.Make_dir(pathSharing)
        ExportFBXOption(fbxPath)
    else:
        cmds.warning("Chưa chọn object để share!")
        cmds.confirmDialog(title="Error",
                           message="Chưa chọn object để share!",
                           button=["Confirm Export"])

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

    print("Import thành công !!!")
    cmds.confirmDialog(title="Success",
                       message="Import thành công !!!",
                       button=["Confirm"])

def blenderToMaya():
    name = f'{username}_Blender.fbx'
    fbxPath = os.path.join(blenderPath, name)
    if os.path.exists(fbxPath):
        CommonPyFunction.Make_dir(blenderPath)
        importFBXOption(fbxPath)
    else:
        cmds.warning(" Không có file nào để import !!!")
        cmds.confirmDialog(title="Warning",
                           message="Không có file nào để import !!!",
                           button=["Confirm"])

def unrealToMaya():
    name = f'{username}_Unreal.fbx'
    fbxPath = os.path.join(UnrealPath, name)
    if os.path.exists(fbxPath):
        CommonPyFunction.Make_dir(UnrealPath)
        importFBXOption(fbxPath)
    else:
        cmds.warning(" Không có file nào để import !!!")
        cmds.confirmDialog(title="Warning",
                           message="Không có file nào để import !!!",
                           button=["Confirm"])


def unityToMaya():
    name = f'{username}_Unity.fbx'
    fbxPath = os.path.join(UnityPath, name)
    if os.path.exists(fbxPath):
        CommonPyFunction.Make_dir(UnityPath)
        importFBXOption(fbxPath)
    else:
        cmds.warning(" Không có file nào để import !!!")
        cmds.confirmDialog(title="Warning",
                           message="Không có file nào để import !!!",
                           button=["Confirm"])


def clean_gs_junk():
    # Tìm tất cả junk group (bao gồm cả nested)
    junk_nodes = cmds.ls(type="transform", long=True) or []
    junk_nodes = [j for j in junk_nodes if "gsJunkGroup" in j]

    # Sort depth (deepest first để tránh lỗi hierarchy)
    junk_nodes.sort(key=lambda x: x.count("|"), reverse=True)

    for junk in junk_nodes:
        if not cmds.objExists(junk):
            continue

        children = cmds.listRelatives(junk, children=True, fullPath=True) or []

        for child in children:
            try:
                # Unparent ra world
                cmds.parent(child, world=True)
            except:
                pass

        try:
            cmds.delete(junk)
        except:
            pass

    # Clean thêm transform rác (identity)
    all_transforms = cmds.ls(type="transform", long=True) or []
    for node in all_transforms:
        try:
            # bỏ qua camera default
            if cmds.listRelatives(node, shapes=True):
                cmds.makeIdentity(node, apply=True, t=True, r=True, s=True, n=False)
        except:
            pass
