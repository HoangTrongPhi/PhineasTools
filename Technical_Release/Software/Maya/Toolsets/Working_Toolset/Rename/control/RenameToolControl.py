from configparser import DEFAULTSECT

import maya.cmds as cmds
import os
import sys
from maya import OpenMayaUI as omui

from Software.Maya.Toolsets.Working_Toolset.Rename.model.RenameTool import hashRename

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

# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.Rename.UI.Rename as Rename
importlib.reload(Rename)
import Software.Maya.Toolsets.Working_Toolset.Rename.model.RenameTool as RenameTool
importlib.reload(RenameTool)

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

class RenameToolControl(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ MeshPosition Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(RenameToolControl, self).__init__(parent=parent)

        # Tạo một instance của lớp UI từ file MeshPosition.py
        # Dùng phương thức setupUi để áp dụng giao diện vào QMainWindow này
        self.ui = Rename.Ui_mainWindow()
        self.ui.setupUi(self)

        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("RenameToolControl_window")
        self.setWindowTitle("Rename Tool")

        # Các phương thức createWidgets và createLayouts không cần thiết
        # vì self.ui.setupUi(self) đã tạo tất cả widget và layout.
        self.createWidgets()
        self.createLayouts()


        # Kết nối các tín hiệu (signal) từ widget tới các hàm (slot)
        self.createConnection()

        self.setup_connections()
        self.on_mode_checkbox_toggled()
    def createWidgets(self):
        """
        Tất cả các widget đã được tạo bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm hoặc thêm Parameter
        của widget nếu cần.
        """
        #################################

        # Rename Base (mode=3)
        self.ui.txt_Rename.setText("Your_Object_Name")
        self.ui.chkb_3.setChecked(True)

        # Rename and Number
        self.ui.dsb_Start.setValue(1)
        self.ui.dsb_Padding.setValue(2)

        # Before  (mode=1), After (mode=2)
        self.ui.txt_AddBefore.setText("prefix_")
        self.ui.txt_AddAfter.setText("_suffix")

        ##################################

        # Hash Rename
        self.ui.txt_HashRename.setText("name_####_suffix")

        self.ui.txt_Search.setText("pasted_")


    def createLayouts(self):
        """
        Layout đã được thiết lập bởi self.ui.setupUi(self).
        Phương thức này có thể dùng để tùy chỉnh thêm các Layouts nếu cần.
        """
        pass

    def setup_connections(self):
        # Kết nối các checkbox với một slot duy nhất
        self.ui.chkb_1.toggled.connect(self.on_mode_checkbox_toggled)
        self.ui.chkb_2.toggled.connect(self.on_mode_checkbox_toggled)
        self.ui.chkb_3.toggled.connect(self.on_mode_checkbox_toggled)

    def on_mode_checkbox_toggled(self):
        # Nếu chkb_1 được bật -> tắt chkb_2 và chkb_3
        if self.ui.chkb_1.isChecked():
            self.ui.chkb_2.setChecked(False)
            self.ui.chkb_3.setChecked(False)
        elif self.ui.chkb_2.isChecked():
            self.ui.chkb_1.setChecked(False)
            self.ui.chkb_3.setChecked(False)
        elif self.ui.chkb_3.isChecked():
            self.ui.chkb_1.setChecked(False)
            self.ui.chkb_2.setChecked(False)

    def createConnection(self):
        """
        Kết nối các nút bấm và widget khác với các hàm xử lý.
        """
        # Rename Base
        self.ui.btn_reNum.clicked.connect(self.RenameNumber_btn)
        self.ui.btn_addBefore.clicked.connect(self.AddBefore_btn)
        self.ui.btn_addAfter.clicked.connect(self.AddAfter_btn)

        self.ui.btn_FirstChar.clicked.connect(self.FirstChar_btn)
        self.ui.btn_LastChar.clicked.connect(self.LastChar_btn)

        self.ui.btn_Rename.clicked.connect(self.HashName_btn)
        self.ui.btn_addBefore.clicked.connect(self.AddBefore_btn)
        self.ui.btn_addAfter.clicked.connect(self.AddAfter_btn)

        self.ui.btn_Pre_01.clicked.connect(self.Pre_01_btn)
        self.ui.btn_Pre_02.clicked.connect(self.Pre_02_btn)
        self.ui.btn_Pre_03.clicked.connect(self.Pre_03_btn)
        self.ui.btn_Pre_04.clicked.connect(self.Pre_04_btn)
        self.ui.btn_Pre_05.clicked.connect(self.Pre_05_btn)
        self.ui.btn_Pre_06.clicked.connect(self.Pre_06_btn)

        self.ui.btn_Replace.clicked.connect(self.Replace_btn)

        self.ui.btn_pkgSort.clicked.connect(self.PkgSort_btn)
        self.ui.btn_pkgCleanGroup.clicked.connect(self.PkgClean_group_btn)
        self.ui.btn_pkgReset.clicked.connect(self.PkgReset_btn)

        # btnFAQs
        self.ui.btn_FAQsAll.clicked.connect(self.FAQsAll_btn)
        self.ui.btn_FAQsHash.clicked.connect(self.FAQsHash_btn)
        self.ui.btn_FAQsSearch.clicked.connect(self.FAQsSearch_btn)
        self.ui.btn_FAQsAddPrefix.clicked.connect(self.FAQsAddPrefix_btn)



    # ============== SLOTS ==============
    # Các hàm này sẽ được gọi khi người dùng tương tác với giao diện.
    # Viết logic xử lý cho Maya vào đây.
    # ===================================
    def FAQsAll_btn(self):
        cmds.confirmDialog(m="")

    def FAQsHash_btn(self):
        cmds.confirmDialog(m="")

    def FAQsSearch_btn(self):
        cmds.confirmDialog(m="")

    def FAQsAddPrefix_btn(self):
        cmds.confirmDialog(m="")

    def RenameNumber_btn(self):
        # Lấy dữ liệu từ UI Rename and Number
        start = self.ui.dsb_Start.value()
        padding = self.ui.dsb_Padding.value()
        prefix = self.ui.txt_AddBefore.toPlainText()
        suffix = self.ui.txt_AddAfter.toPlainText()
        rename_base = self.ui.txt_Rename.toPlainText()

        # Xác định chế độ dựa trên checkbox nào đang bật
        if self.ui.chkb_1.isChecked():
            mode = 1  # Thêm tiền tố
        elif self.ui.chkb_2.isChecked():
            mode = 2  # Thêm hậu tố
        elif self.ui.chkb_3.isChecked():
            mode = 3  # Đặt tên theo số
        else:
            cmds.warning("Chưa chọn chế độ đổi tên!")
            return

        # Gọi hàm đổi tên
        RenameTool.rename_objects(
            mode=mode,
            prefix=prefix,
            suffix=suffix,
            rename_base=rename_base,
            start=start,
            padding=padding
        )

    def AddBefore_btn(self):
        # Lấy dữ liệu từ UI Rename and Number
        prefix = self.ui.txt_AddBefore.toPlainText()
        RenameTool.rename_objects(mode=1, prefix=prefix)

    def AddAfter_btn(self):
        # Lấy dữ liệu từ UI Rename and Number
        suffix = self.ui.txt_AddAfter.toPlainText()
        RenameTool.rename_objects(mode=2, suffix = suffix)


    def FirstChar_btn(self):
        RenameTool.remove_first_char_from_selection()

    def LastChar_btn(self):
        RenameTool.remove_last_char_from_selection()


    def HashName_btn(self):
        pattern = self.ui.txt_HashRename.toPlainText()     #Nếu là QTextEdit , '.text()' nếu là QLineEdit
        if pattern:
            RenameTool.hashRename(pattern)
            cmds.select()

    def Replace_btn(self):
        print(" kích hoạt")


    def Pre_01_btn(self):
        Prefix_Name = "Grp_"
        return [cmds.rename(obj,Prefix_Name + obj.split('|')[-1])
                for obj in cmds.ls(sl=True, long=True)]


    def Pre_02_btn(self):
        Prefix_Name = "MI_"
        return [cmds.rename(obj,Prefix_Name + obj.split('|')[-1])
                for obj in cmds.ls(sl=True, long=True)]

    def Pre_03_btn(self):
        Prefix_Name = "SM_"
        return [cmds.rename(obj,Prefix_Name + obj.split('|')[-1])
                for obj in cmds.ls(sl=True, long=True)]

    def Pre_04_btn(self):
        Prefix_Name = "SKM_"
        return [cmds.rename(obj, Prefix_Name + obj.split('|')[-1])
                for obj in cmds.ls(sl=True, long=True)]

    def Pre_05_btn(self):
        Suffix_Name = "_pkg"
        return [cmds.rename(obj, obj.split('|')[-1] + Suffix_Name)
                for obj in cmds.ls(sl=True, long=True)]

    def Pre_06_btn(self):
        Suffix_Name = "_More"
        return [cmds.rename(obj, obj.split('|')[-1] + Suffix_Name)
                for obj in cmds.ls(sl=True, long=True)]

    #Làm sau
    def PkgSort_btn(self):
        print("Kích hoạt")
    def PkgClean_group_btn(self):
        print("Kích hoạt")
    def PkgReset_btn(self):
        print("Kích hoạt")


def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "RenameToolControl_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    # Tạo và hiển thị cửa sổ tool
    mainWin = RenameToolControl(parent=mayaMainWindow)
    mainWin.setObjectName("RenameToolControl_window")
    mainWin.show()
    return mainWin



openWindow()
