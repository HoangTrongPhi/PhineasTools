import maya.cmds as cmds
import os
import sys
from maya import OpenMayaUI as omui


try:
    from shiboken2 import wrapInstance

    from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QIODevice
    from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QFileDialog
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    from shiboken6 import wrapInstance

    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QPushButton, QFileDialog
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt

from functools import partial  # passing args during signal function calls

import importlib

import Common.Python.CommonPyFunction as CommonPyFunction
importlib.reload(CommonPyFunction)

import Common.CommonHelpers as CommonHelpers
importlib.reload(CommonHelpers)

import Software.Maya.Toolsets.Working_Toolset.MeshPosition.model.MeshPosTool as MeshPosTool
importlib.reload(MeshPosTool)

import Libs.TransformFunction as TransformFunction
importlib.reload(TransformFunction)

# Import file UI đã được convert
import Software.Maya.Toolsets.Working_Toolset.MeshPosition.UI.MeshPosition as MeshPosition
importlib.reload(MeshPosition)

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

class UL_Controller(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ MeshPosition Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(UL_Controller, self).__init__(parent=parent)

        # Tạo một instance của lớp UI từ file MeshPosition.py
        # Dùng phương thức setupUi để áp dụng giao diện vào QMainWindow này
        self.ui = MeshPosition.Ui_mainWindow()
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
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "UL_Controller_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    # Tạo và hiển thị cửa sổ tool
    mainWin = UL_Controller(parent=mayaMainWindow)
    mainWin.setObjectName("UL_Controller_window")
    mainWin.show()
    return mainWin



openWindow()
