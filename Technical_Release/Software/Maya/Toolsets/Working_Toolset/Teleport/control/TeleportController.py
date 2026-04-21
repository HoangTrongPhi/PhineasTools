"""
    Author: HOANG TRONG PHI
    20/4/2026
"""


import maya.cmds as cmds
import os

import gc   # bắt maya xóa GUI thừa, giải phóng bộ nhớ garbage clear
import getpass

from Software.Maya.Toolsets.Working_Toolset.Teleport.model.TeleportFBX import mainPath

username = getpass.getuser()


from maya import OpenMayaUI as omui
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance


import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

import Libs.NamingConvention as NamingConvention
importlib.reload(NamingConvention)

#file UI
import Software.Maya.Toolsets.Working_Toolset.Teleport.UI.TeleportTool_UI as TeleportTool_UI
importlib.reload(TeleportTool_UI)

#file model
import Software.Maya.Toolsets.Working_Toolset.Teleport.model.TeleportFBX as TeleportFBX
importlib.reload(TeleportFBX)


def getDirectoryofModule(modulename):
    """
    Input: module as string
    OUtput:
        List: name as string and directory of module
    """
    module = modulename
    try:
        module = importlib.import_module(modulename)        # importlib.import_module(name, package)
    except:
        pass

    currWD = os.path.dirname(module.__file__)
    return currWD

#####
def getMayaMainWindow():
    """Lấy cửa sổ chính của Maya."""
    main_window_ptr = omui.MQtUtil.mainWindow()
    if main_window_ptr is not None:
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)
    return None

class Teleport_Controller(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ Teleport Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(Teleport_Controller, self).__init__(parent=parent)

        # Tạo một instance của lớp UI từ file Teleport.py
        # Dùng phương thức setupUi để áp dụng giao diện vào QMainWindow này
        self.ui = TeleportTool_UI.Ui_mainWindow()
        self.ui.setupUi(self)

        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("TeleportTool_window")
        self.setWindowTitle("TeleportTool")

        # Các phương thức createWidgets và createLayouts không cần thiết
        # vì self.ui.setupUi(self) đã tạo tất cả widget và layout.
        self.createWidgets()
        self.createLayouts()


        # Kết nối các tín hiệu (signal) từ widget tới các hàm (slot)
        self.createConnection()



    def createWidgets(self):
        """
        Tất cả các widget đã được tạo bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm hoặc thêm Parameter
        của widget nếu cần.
        """
        pass


    def createLayouts(self):
        """
        Layout đã được thiết lập bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm các Layouts nếu cần.
        """
        pass

    def createConnection(self):
        """
        Kết nối các nút bấm và widget khác với các hàm xử lý.
        """
        self.ui.btExptBlender.clicked.connect(self.exportToBlender)
        self.ui.btnImptMaya.clicked.connect(self.importToMaya)

        # advanced
        self.ui.btnExportExplore.clicked.connect(self.onBrowseFolder)
        self.ui.btnExptOBJ.clicked.connect(self.objExport)
        self.ui.btnExptFBX.clicked.connect(self.exportCustom)
        self.ui.btnExptUSD.clicked.connect(self.usdExport)
        self.ui.btnOpenExplore.clicked.connect(self.openExplorer)

        # engine2maya
        self.ui.btnUnityToMaya.clicked.connect(self.fromUnityToMaya)
        self.ui.btnUnrealToMaya.clicked.connect(self.fromUnrealToMaya)
        # maya2engine
        self.ui.btnExptUE.clicked.connect(self.fromMayaToUnreal)
        self.ui.btnExptUnity.clicked.connect(self.fromMayaToUnity)

        # FAQs btn
        self.ui.btnFAQs_MaBlen.clicked.connect(self.mayaToBlenderFAQs)
        self.ui.btnFAQs_Advanced.clicked.connect(self.AdvancedFAQs)
        self.ui.btnFAQs_Engine.clicked.connect(self.EngineFAQs)


    # FAQs
    def mayaToBlenderFAQs(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message="Import file Blender to Maya,"
                                    "\nExport file Maya to Blender"
                                    "\nLưu ý: Chỉ export được mesh, không hỗ trợ rig, animation",
                           button=["Đã hiểu"])



    def AdvancedFAQs(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message="Chọn folder cần lưu,"
                                   "\nPath sẽ được hiển thị trên Box"
                                    "\nLưu ý: Chỉ export được mesh, không hỗ trợ rig, animation"
                                    "\nObj và USD update sau",
                           button=["Đã hiểu"])

    def EngineFAQs(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message="Tạo từng cặp BakeSet Low/High")

    def exportToBlender(self):
        TeleportFBX.exportToBlender()

    def importToMaya(self):
        TeleportFBX.blenderToMaya()

    # Advanced
    # ---------Explore Browser---------------
    def onBrowseFolder(self):
        if not CommonHelpers.CheckValidScene():
            return

        folderPath = CommonHelpers.browseFolderPath()
        if folderPath:
            self.exportPath = folderPath  # lưu lại path
            self.ui.textEditPath.setPlainText(folderPath)

    def exportCustom(self):
        finalPath = getattr(self, "exportPath", None)

        if not finalPath:
            cmds.warning("Chưa chọn đường dẫn export!")
            return

        if cmds.ls(sl=True):
            meshName = NamingConvention.getSelMeshName()
            name = f'{meshName}.fbx'
            fbxPath = os.path.join(finalPath, name)
            fbxPath = os.path.normpath(fbxPath).replace("\\", "/")

            TeleportFBX.ExportFBXOption(fbxPath)
        else:
            cmds.warning("Chưa chọn object để export!")
            cmds.confirmDialog(title="Error",
                               message="Chưa chọn object để export!",
                               button=["Confirm Export"])



    def objExport(self):
        cmds.confirmDialog(title="Thông báo",
                           message="Chưa cập nhật!",
                           button=["Đã hiểu"])

    def usdExport(self):
        cmds.confirmDialog(title="Thông báo",
                           message="Chưa cập nhật!",
                           button=["Đã hiểu"])

    def openExplorer(self):
        finalPath = self.ui.textEditPath.toPlainText()
        if finalPath:
            CommonHelpers.folderExploreBrowser(finalPath)
        else:
            cmds.warning("Chưa chọn đường dẫn export!")
            cmds.confirmDialog(title="Warning",
                               message="Không mở được folder!"
                                "\nVui lòng chọn đường dẫn hợp lệ và thử lại.",
                               button=["Đã hiểu"])

    # Sharing file
    def ExportShare(self):
        TeleportFBX.exportFBXSharing()

    def importShare(self):
        pass

    def shareExplorer(self):
        pass

    # import Engine to Maya
    def fromUnityToMaya(self):
        TeleportFBX.unityToMaya()
        TeleportFBX.clean_gs_junk()

    def fromUnrealToMaya(self):
        TeleportFBX.unrealToMaya()
        TeleportFBX.clean_gs_junk()

    # export Maya to Engine
    def fromMayaToUnreal(self):
        finalPath = self.ui.textEditPath.toPlainText()

        if not finalPath:
            cmds.warning("Chưa chọn đường dẫn export!")
            return

        # thêm folder con
        finalPath = os.path.join(finalPath, "AssetUnreal")

        # normalize cho Maya
        finalPath = os.path.normpath(finalPath).replace("\\", "/")

        if cmds.ls(sl=True):
            meshName = NamingConvention.getSelMeshName()
            name = f'{meshName}.fbx'
            fbxPath = os.path.join(finalPath, name)
            fbxPath = os.path.normpath(fbxPath).replace("\\", "/")

            # tạo folder nếu chưa có
            if not os.path.exists(finalPath):
                os.makedirs(finalPath)

            TeleportFBX.ExportFBXOption(fbxPath)
        else:
            cmds.warning("Chưa chọn object để export!")


    def fromMayaToUnity(self):
        finalPath = self.ui.textEditPath.toPlainText()

        if not finalPath:
            cmds.warning("Chưa chọn đường dẫn export!")
            return

        # thêm folder con
        finalPath = os.path.join(finalPath, "AssetUnity")

        # normalize cho Maya
        finalPath = os.path.normpath(finalPath).replace("\\", "/")

        if cmds.ls(sl=True):
            meshName = NamingConvention.getSelMeshName()
            name = f'{meshName}.fbx'
            fbxPath = os.path.join(finalPath, name)
            fbxPath = os.path.normpath(fbxPath).replace("\\", "/")

            # tạo folder nếu chưa có
            if not os.path.exists(finalPath):
                os.makedirs(finalPath)

            TeleportFBX.ExportFBXOption(fbxPath)
        else:
            cmds.warning("Chưa chọn object để export!")



def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "TeleportTool_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    gc.collect()
    # Tạo và hiển thị cửa sổ tool
    mainWin = Teleport_Controller(parent=mayaMainWindow)
    mainWin.setObjectName("TeleportTool_window")
    mainWin.show()
    return mainWin

openWindow()
