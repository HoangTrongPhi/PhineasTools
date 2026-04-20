"""
    Author: HOANG TRONG PHI
    20/4/2026
"""


import maya.cmds as cmds
import os
import sys
import gc   # bắt maya xóa GUI thừa, giải phóng bộ nhớ garbage clear
import json

from maya import OpenMayaUI as omui

from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

from functools import partial  # passing args during signal function calls

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.Teleport.UI.TeleportTool_UI as TeleportTool_UI
importlib.reload(TeleportTool_UI)

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
        self.setObjectName("UL_Controller_window")
        self.setWindowTitle("UL_Controller")

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
        #self.ui.btn_slots_function.clicked.connect(self.slots_function)


    # ============== SLOTS ==============
    # Các hàm này sẽ được gọi khi người dùng tương tác với giao diện.
    # Viết logic xử lý cho Maya vào đây.
    # ===================================

    def slots_function(self):
        pass


def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "Teleport_Controller_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    gc.collect()
    # Tạo và hiển thị cửa sổ tool
    mainWin = Teleport_Controller(parent=mayaMainWindow)
    mainWin.setObjectName("Teleport_Controller_window")
    mainWin.show()
    return mainWin



openWindow()
