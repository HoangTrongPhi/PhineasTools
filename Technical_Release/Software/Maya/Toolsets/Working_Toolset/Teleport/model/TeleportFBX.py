"""
    Hoang Trọng Phi
    16/6/2025 Đã chỉnh lại một số bug
"""


import os
import importlib
import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)
import maya.mel as mel, maya.cmds as cmds


import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

# thêm adminList

import getpass
adminList = ['Phineas', 'trong','HuangFei']
username = getpass.getuser()
mainPath = 'C:/tempMaya/ExportFBX/'

pathSharing = 'C:/tempMaya/ExportFBX/Share' # thêm pathSharing vào
if not os.path.exists(pathSharing):
    pathSharing =  '            '


###################################################################
#                   EXPORT
###################################################################
def ExportFBXOption(filename, FBXversion='FBX202000', FBXASCII=True, unit='cm', selection=True):

    # Load FBX plugin nếu chưa có
    if not cmds.pluginInfo('fbxmaya', query=True, loaded=True):
        try:
            cmds.loadPlugin('fbxmaya', quiet=True)
            #cmds.confirmDialog(message=("Đã load plugin FBX thành công"))
        except:
            cmds.confirmDialog(message=("Không thể load plugin FBX."))

    # Flag thực thi FBX
    mel.eval('FBXExportSmoothingGroups -v true;')
    mel.eval('FBXExportHardEdges -v false;')
    mel.eval('FBXExportTangents -v true;')
    mel.eval('FBXExportSmoothMesh -v false;')
    mel.eval('FBXExportInstances -v false;') # Có thể cần đặt thành true nếu muốn xuất instance
    mel.eval('FBXExportReferencedAssetsContent -v false;')
    mel.eval('FBXExportAnimationOnly -v false;')
    mel.eval('FBXExportApplyConstantKeyReducer -v false;')
    mel.eval('FBXExportBakeComplexAnimation -v false;')
    mel.eval('FBXExportBakeResampleAnimation -v false;')
    mel.eval('FBXExportCacheFile -v false;')
    mel.eval('FBXExportColladaSingleMatrix false;')
    mel.eval('FBXExportColladaTriangulate false;')
    mel.eval('FBXExportConstraints -v false;')
    mel.eval('FBXExportInstances -v false;')
    mel.eval('FBXExportShapes -v false;')
    mel.eval('FBXExportSkins -v false;') # thay đổi thành true nếu muốn xuất skinning
    mel.eval('FBXExportTriangulate -v false;')
    mel.eval('FBXExportUseSceneName -v false;')
    mel.eval('FBXExportCameras -v false;') # Đặt thành true nếu muốn xuất camera
    mel.eval('FBXExportLights -v false;')  # Đặt thành true nếu muốn xuất đèn
    mel.eval('FBXExportEmbeddedTextures -v false;')
    mel.eval(('FBXExportConvertUnitString {};').format(unit))
    mel.eval(('FBXExportFileVersion {};').format(FBXversion))
    if FBXASCII == False:
        mel.eval('FBXExportInAscii -v false;')
    else:
        mel.eval('FBXExportInAscii -v true;')
    mel.eval('FBXExportUpAxis "y";')
    mel.eval('FBXExportGenerateLog -v false;')
    if selection == True:
        mel.eval(('FBXExport -f "{}" -s;').format(filename))
    else:
        mel.eval(('FBXExport -f "{}";').format(filename))

    cmds.confirmDialog(message=("Export thành công"))
    return
    ExportFBXOption()


def exportFBX():
    currSel = cmds.ls(sl=True, l=True)
    name = ('{}_Maya.fbx').format(username)
    fbxPath = mainPath + name
    if cmds.ls(sl=True, l=True):
        CommonPyFunction.Make_dir(mainPath)     # Xuất đúng file FBX vào path đã save scene
        ExportFBXOption(fbxPath)



####

# Dùng chính 'temp/Export/Share' để lưu trữ file fbx share
def exportFBXSharing():
    currSel = cmds.ls(sl=True, l=True)
    name = ('{}_working.fbx').format(username)
    fbxPath = pathSharing + name
    if cmds.ls(sl=True, l=True):
        CommonPyFunction.Make_dir(pathSharing)
        ExportFBXOption(fbxPath)


def exportFBXFolder(suffix='', FBXversion='FBX202000', FBXASCII=True, unit='cm', folderExport='', selection=True,
                    name=''):
    """
    Export từng mesh được chọn ra từng file FBX riêng biệt.

    Parameters:
        suffix (str): Hậu tố thêm vào tên file FBX (ví dụ: '_Low').
        FBXversion (str): Phiên bản FBX để export (ví dụ: 'FBX202000').
        FBXASCII (bool): Export ở dạng ASCII nếu True, binary nếu False.
        unit (str): Đơn vị scale ('cm', 'm', 'in', v.v.).
        folderExport (str): Đường dẫn thư mục nơi lưu các file FBX.
        selection (bool): Nếu True, chỉ export các object được chọn.
        name (str): Tên file FBX cố định (ghi đè tên object).

    Returns:
        int: Luôn trả về 1 sau khi chạy xong.
    """
    scenePath = CommonHelpers.GetScenePath()
    currSel = cmds.ls(selection=True, long=True)     # Lưu danh sách object đang được chọn (full path)
    if CommonHelpers.CheckValidScene():     # Kiểm tra scene hiện tại có hợp lệ không (ví dụ: đã được lưu)
        if cmds.ls(selection=True, long=True):
            # Lặp qua từng object được chọn
            for objLongName in cmds.ls(selection=True, long=True):
                # Lấy tên ngắn (short name) của object (không kèm path '|')
                objShortname = cmds.ls(objLongName, shortNames=True)[0].split('|')[-1]
                tempfolderExport = scenePath    # Mặc định sử dụng đường dẫn scene làm nơi export
                if name != '':                  # Nếu user có nhập tên cố định thì dùng thay cho tên object
                    objShortname = name

                # Nếu user có cung cấp thư mục export, dùng nó thay thế
                if folderExport != '':
                    tempfolderExport = folderExport
                    # Tạo thư mục export nếu chưa có
                    CommonPyFunction.Make_dir(tempfolderExport)
                # Tạo đường dẫn tới file FBX (có hoặc không hậu tố)
                if suffix == '':
                    fbxPath = tempfolderExport + '/' + objShortname + '.fbx'
                else:
                    fbxPath = tempfolderExport + '/' + objShortname + ('_{}.fbx').format(suffix)

                # Chỉ chọn object hiện tại để export
                cmds.select(objLongName)
                # In ra console đường dẫn đang export để debug
                print(fbxPath)
                # Gọi hàm export FBX với thông tin cấu hình
                ExportFBXOption(fbxPath, FBXversion, FBXASCII, unit)
            # Sau khi export xong, chọn lại các object ban đầu
            cmds.select(currSel)
            # Mở thư mục chứa các file FBX
            os.startfile(tempfolderExport)
        else:
            # Nếu không có object nào được chọn thì hiện hộp thoại cảnh báo
            cmds.confirmDialog(m='Cần chọn object để export!')
    # Trả về 1 luôn, có thể thay đổi thành True nếu cần rõ hơn
    return 1


def exportFBXFolderScene(suffix='', FBXversion='FBX202000', FBXASCII=True, unit='cm', folderExport='', selection=False, name=''):
    """
        Export nguyen scene thanh 1 file FBX
    """
    scenePath = CommonHelpers.GetScenePath()
    sceneName = CommonHelpers.GetSceneName()
    if CommonHelpers.CheckValidScene():
        currSel = cmds.ls(selection=True, long=True)
        tempFolderPath = scenePath
        if name != '':
            sceneName = name
        if folderExport != '':
            tempfolderExport = folderExport
            CommonPyFunction.Make_dir(tempfolderExport)
        if suffix == '':
            fbxPath = tempfolderExport + '/' + sceneName + '.fbx'
        else:
            fbxPath = tempfolderExport + '/' + sceneName + ('_{}.fbx').format(suffix)
        print (fbxPath)
        ExportFBXOption(fbxPath, FBXversion, FBXASCII, unit, selection)
        cmds.select(currSel)
        os.startfile(tempFolderPath)
    return 1



###################################################################
#                   IMPORT
###################################################################

def ImportFile(file):
    if os.path.exists(file):
        shadingNetworksOptVar = cmds.optionVar(q='removeDuplicateShadingNetworksOnImport')
        cmds.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', 1))
        cmds.file(file, i=True, defaultNamespace=True, removeDuplicateNetworks=True, ignoreVersion=True)
        cmds.optionVar(intValue=('removeDuplicateShadingNetworksOnImport', shadingNetworksOptVar))
    return 1


def importFBX(unlockNormal=True):
    name = ('{}_FromMax.fbx').format(username)
    fbxPath = mainPath + name
    if os.path.exists(fbxPath):
        importFBXOption(fbxPath, unlockNormal)
    else:
        print ('Không tìm thấy file để IMPORT')


def importFBXFromSharing(user):
    user = user.lower()
    name = ('{}_working.fbx').format(user)
    fbxPath = pathSharing + name
    if os.path.exists(fbxPath):
        importFBXOption(fbxPath)
    else:
        cmds.confirmDialog(message=('Không tìm thấy file của User: {}').format(user))

def importFBXOption(filename, unlockNormals=True):
    print ('unlockNormal: {}').format(unlockNormals)
    mel.eval('FBXImportMode -v add;')
    mel.eval('FBXImportHardEdges  -v false;')
    mel.eval('FBXImportUpAxis  "y";')
    mel.eval('FBXImportConvertUnitString  "cm";')
    if unlockNormals == False:
        mel.eval('FBXImportUnlockNormals -v false;')
    else:
        mel.eval('FBXImportUnlockNormals -v true;')
    mel.eval('FBXImportGenerateLog  -v true;')
    mel.eval('FBXImportShowUI -v false;')
    mel.eval('FBXImportCameras  -v true;')
    mel.eval(('FBXImport  -file "{}";').format(filename))



