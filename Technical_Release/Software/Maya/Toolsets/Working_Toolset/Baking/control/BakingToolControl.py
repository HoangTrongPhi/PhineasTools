"""
Hoang Trong Phi
created 12/6/2025

"""
import maya.cmds as cmds
import os
import sys
from maya import OpenMayaUI as omui

#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

from functools import partial  # passing args during signal function calls

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

import Libs.TransformFunction as TransformFunction
importlib.reload(TransformFunction)

import Libs.SortOutliner as SortOutliner
importlib.reload(SortOutliner)

# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.Baking.UI.BakeTool as BakeTool
importlib.reload(BakeTool)
import Software.Maya.Toolsets.Working_Toolset.Baking.model.Baking_MayaFuntion as Baking_MayaFuntion
importlib.reload(Baking_MayaFuntion)
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

class BakingToolControl(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ MeshPosition Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(BakingToolControl, self).__init__(parent=parent)

        # Tạo một instance của lớp UI từ file MeshPosition.py
        # Dùng phương thức setupUi để áp dụng giao diện vào QMainWindow này
        self.ui = BakeTool.Ui_mainWindow()
        self.ui.setupUi(self)

        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("BakingToolControl_window")
        self.setWindowTitle("Baking Tool Control")

        # Các phương thức createWidgets và createLayouts không cần thiết
        # vì self.ui.setupUi(self) đã tạo tất cả widget và layout.
        self.createWidgets()
        self.createLayouts()


        # Kết nối các tín hiệu (signal) từ widget tới các hàm (slot)
        self.createConnection()

        self.current_index = None  # Lưu chỉ số hiện tại
        self.max_index = None  # Lưu chỉ số lớn nhất

    def createWidgets(self):
        """
        Tất cả các widget đã được tạo bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm hoặc thêm Parameter
        của widget nếu cần.
        """
        # QTextEdit

        self.ui.textEditPath.setText(" Get Export Path Here: // ")

        # QDoubleSpinBox
        self.ui.spinBoxDis.setValue(2)

    def createLayouts(self):
        """
        Layout đã được thiết lập bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm các Layouts nếu cần.
        """
        pass

    def createConnection(self):
        #Your code goes here

        ######
        self.ui.btnBakeSet.clicked.connect(self.createBakeset_btn)

        self.ui.spinBoxDis.valueChanged.connect(self.explode_btn)
        self.ui.btnDisExplode.clicked.connect(self.explode_btn)
        self.ui.btnDisReset.clicked.connect(self.reset_explode_btn)

        self.ui.btnDisSwap.clicked.connect(self.swapHighLow)

        self.ui.btnDisHigh.clicked.connect(self.showDisHigh)
        self.ui.btnDisLow.clicked.connect(self.showDisLow)

        self.ui.btnSelectHigh.clicked.connect(self.SelectHigh_btn)
        self.ui.btnSelectLow.clicked.connect(self.SelectLow_btn)
        self.ui.btnSelectPair.clicked.connect(self.SelectPair_btn)
        self.ui.btnSelectBigToSmall.clicked.connect(self.SelectBigToSmall_btn)
        self.ui.btnSelectSmallToBig.clicked.connect(self.SelectSmallToBig_btn)

        self.ui.btnExportHigh.clicked.connect(self.exportHigh_btn)
        self.ui.btnExportLow.clicked.connect(self.exportLow_btn)
        self.ui.btnExportAll.clicked.connect(self.exportOneFBX)

        self.ui.btnExportExplore.clicked.connect(self.onBrowseFolder)
        self.ui.btnExportSpecial.clicked.connect(self.ExportCustom)

        self.ui.btnFAQs_all.clicked.connect(self.createFAQs_all_btn)
        self.ui.btnFAQs_display.clicked.connect(self.createFAQs_display_btn)
        self.ui.btnFAQs_select.clicked.connect(self.createFAQs_select_btn)
        self.ui.btnFAQs_export.clicked.connect(self.createFAQs_export_btn)
        ########################
    def createFAQs_all_btn(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message = "Tạo từng cặp BakeSet Low/High")

    def createFAQs_display_btn(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message = " Hiển thị High/Low sau khi tạo BakeSet")

    def createFAQs_select_btn(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message = "Select nhanh High/Low hoặc Pair (cả hai)")

    def createFAQs_export_btn(self):
        cmds.confirmDialog(title=" Hướng dẫn",
                           message="Có 2 Option để Export"
                                   "\nHoặc là explore tìm kiếm thư mục"
                                   "\nHoặc là dán Path vào ô trống")

    def createBakeset_btn(self):
        Baking_MayaFuntion.createBakeset()

    # Display
    def showDisHigh(self):
        Baking_MayaFuntion.toggleGroup("|High")

    def showDisLow(self):
        Baking_MayaFuntion.toggleGroup("|Low")

    def swapHighLow(self):
        Baking_MayaFuntion.swapHighLow()

    # Explode
    def explode_btn(self,number):
        number = format(number)
        Baking_MayaFuntion.explode()

    def reset_explode_btn(self):
        Baking_MayaFuntion.resetExplode()


    # Select
    def SelectHigh_btn(self):
        Baking_MayaFuntion.selectHigh()

    def SelectLow_btn(self):
        Baking_MayaFuntion.selectLow()

    def SelectPair_btn(self):
        Baking_MayaFuntion.selectPair()

    def SelectBigToSmall_btn(self):
        """
        Gọi hàm chọn mesh từ Baking_MayaFuntion,
        mỗi lần nhấn nút sẽ giảm index theo thứ tự từ lớn đến nhỏ.
        """
        group = '|High'
        if not cmds.objExists(group):
            return
        # Sort để đảm bảo thứ tự đúng trước khi đếm số lượng
        cmds.select(group, replace=True)
        SortOutliner.sortSelectedGroupByAlphabet()

        mesh_list = cmds.listRelatives(group, children=True, fullPath=True) or []
        if not mesh_list:
            return
        # Khởi tạo index nếu chưa có
        if self.max_index is None or self.current_index is None:
            self.max_index = len(mesh_list) - 1
            self.current_index = self.max_index
        else:
            # Giảm index, nếu < 0 thì quay lại max
            self.current_index -= 1
            if self.current_index < 0:
                self.current_index = self.max_index
        # Gọi hàm từ module
        Baking_MayaFuntion.select_bakeset_by_index(self.current_index)

    def SelectSmallToBig_btn(self):
        """
        Gọi hàm chọn mesh từ Baking_MayaFuntion,
        mỗi lần nhấn nút sẽ tăng index theo thứ tự từ nhỏ đến lớn.
        """
        group = '|High'
        if not cmds.objExists(group):
            return
        # Sort để đảm bảo thứ tự đúng trước khi đếm số lượng
        cmds.select(group, replace=True)
        SortOutliner.sortSelectedGroupByAlphabet()
        mesh_list = cmds.listRelatives(group, children=True, fullPath=True) or []
        if not mesh_list:
            return
        # Khởi tạo index nếu chưa có
        if self.max_index is None or self.current_index is None:
            self.max_index = len(mesh_list) - 1
            self.current_index = 0
        else:
            # Tăng index, nếu vượt max thì quay về 0
            self.current_index += 1
            if self.current_index > self.max_index:
                self.current_index = 0
            # Gọi hàm từ module
        Baking_MayaFuntion.select_bakeset_by_index(self.current_index)

    #----------------------------------------------------
    # Logic Lấy Export Folder
    # Nếu customPath hợp lệ, save tại đó, nếu không save tại SaveScenePath
    def getExportFolder(self):
        folderPath = self.getFolderPath()

        if folderPath and os.path.exists(folderPath):
            folderExport = folderPath.replace("\\", "/")
        else:
            scenePath = CommonHelpers.GetScenePath()
            folderExport = scenePath.replace("\\", "/") if scenePath else None

        return folderExport

    # Export
    def exportHigh_btn(self):
        suffix = 'High'
        FBXversion = 'FBX202000'
        FBXASCII = True
        unit = 'cm'
        selection = True
        print(suffix + ' ' + FBXversion + ' ' + str(FBXASCII) + ' ' + unit)

        Baking_MayaFuntion.toggleAll(True)
        sceneName = CommonHelpers.GetSceneName()
        if CommonHelpers.CheckValidScene(showDialog=True)== False:
            cmds.confirmDialog(title="Error",
                                message=("Export không thành công"))
        else:
            cmds.select('|High')
            folderExport = self.getExportFolder()
            TeleportFBX.exportFBXFolder(suffix, FBXversion, FBXASCII, unit, folderExport, selection, sceneName)

    def exportLow_btn(self):
        suffix = 'Low'
        FBXversion = 'FBX202000'
        FBXASCII = True
        unit = 'cm'
        selection = True
        print(suffix + ' ' + FBXversion + ' ' + str(FBXASCII) + ' ' + unit)

        Baking_MayaFuntion.toggleAll(True)
        sceneName = CommonHelpers.GetSceneName()
        if CommonHelpers.CheckValidScene(showDialog=True) == False:
            cmds.confirmDialog(title="Error",
                            message=("Export không thành công"))
        else:
            cmds.select('|Low')
            folderExport = self.getExportFolder()
            TeleportFBX.exportFBXFolder(suffix, FBXversion, FBXASCII, unit, folderExport, selection, sceneName)

    def exportOneFBX(self):
        suffix = 'Bakescene'
        FBXversion = 'FBX202000'
        FBXASCII = True
        unit = 'cm'
        selection = True
        print(suffix + ' ' + FBXversion + ' ' + str(FBXASCII) + ' ' + unit)

        Baking_MayaFuntion.toggleAll(True)
        sceneName = CommonHelpers.GetSceneName()
        cmds.select('|High', '|Low')
        if CommonHelpers.CheckValidScene(showDialog=True) == False:
            cmds.confirmDialog(title="Error",
                               message=("Export không thành công"))
        else:
            cmds.select('|High', '|Low')
            folderExport = self.getExportFolder()
            TeleportFBX.exportFBXFolderScene(suffix, FBXversion, FBXASCII, unit, folderExport, selection, sceneName)

    # ---------Explore Browser---------------
    def onBrowseFolder(self):
        if not CommonHelpers.CheckValidScene():
            return  # Thoát nếu scene chưa được lưu
        folderPath = CommonHelpers.browseFolderPath()
        print(folderPath)
        if folderPath:
            self.ui.textEditPath.setPlainText(folderPath)
            return folderPath

    #----------Nhận Path thủ công----------
    def getFolderPath(self):
        folderPath = self.ui.textEditPath.toPlainText().strip()    # strip() loại bỏ khoảng trắng
        if folderPath and os.path.exists(folderPath):
            return folderPath
        else:
            cmds.confirmDialog(title="Error",
                               message="Đường dẫn không hợp lệ!,"
                                       "\nLưu vào Save Scene Path",
                               button=["Confirm Export"])
            return False

    # --------comfirmExport-------------
    def onConfirmExport(self):
        path = self.getFolderPath()
        print(path)
        if not path:
            return

        # tiếp tục xử lý export tại folder `path`

    def ExportCustom(self):
        self.onConfirmExport()



def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "BakingToolControl_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    # Tạo và hiển thị cửa sổ tool
    mainWin = BakingToolControl(parent=mayaMainWindow)
    mainWin.setObjectName("BakingToolControl_window")
    mainWin.show()
    return mainWin



openWindow()

