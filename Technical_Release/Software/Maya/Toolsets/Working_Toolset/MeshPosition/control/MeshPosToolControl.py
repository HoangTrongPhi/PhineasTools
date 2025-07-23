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

class HF_MeshPositionTool(QtWidgets.QMainWindow):
    """
    Controller class cho cửa sổ MeshPosition Tool.
    Lớp này kế thừa QMainWindow để khớp với file UI được tạo ra.
    """
    window = None

    def __init__(self, parent=getMayaMainWindow()):
        """
        Khởi tạo class.
        """
        super(HF_MeshPositionTool, self).__init__(parent=parent)

        # Tạo một instance của lớp UI từ file MeshPosition.py
        # Dùng phương thức setupUi để áp dụng giao diện vào QMainWindow này
        self.ui = MeshPosition.Ui_mainWindow()
        self.ui.setupUi(self)

        # Đặt một objectName duy nhất để dễ dàng tìm và đóng cửa sổ cũ
        self.setObjectName("HF_MeshPositionTool_window")
        self.setWindowTitle("HF Mesh Position Tool")

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
        # --- Cấu hình các Spin Box cho Transform ---
        self.ui.checkBox_Trans.setChecked(True)
        self.ui.spinPosX.setSingleStep(0.1)
        self.ui.spinPosX.setDecimals(3)
        self.ui.spinPosX.setValue(0)
        self.ui.spinPosX.setMaximum(1000000)
        self.ui.spinPosX.setMinimum(-1000000)
        self.ui.spinPosX.setMinimumWidth(30)

        self.ui.spinPosY.setSingleStep(0.1)
        self.ui.spinPosY.setDecimals(3)
        self.ui.spinPosY.setValue(0)
        self.ui.spinPosY.setMaximum(1000000)
        self.ui.spinPosY.setMinimum(-1000000)
        self.ui.spinPosY.setMinimumWidth(30)

        self.ui.spinPosZ.setSingleStep(0.1)
        self.ui.spinPosZ.setDecimals(3)
        self.ui.spinPosZ.setValue(0)
        self.ui.spinPosZ.setMaximum(1000000)
        self.ui.spinPosZ.setMinimum(-1000000)
        self.ui.spinPosZ.setMinimumWidth(30)

        # --- Cấu hình các Spin Box cho Rotate ---
        self.ui.spinRoX.setSingleStep(0.1)
        self.ui.spinRoX.setDecimals(3)
        self.ui.spinRoX.setValue(0)
        self.ui.spinRoX.setMaximum(360)
        self.ui.spinRoX.setMinimum(-360)
        self.ui.spinRoX.setMinimumWidth(30)

        self.ui.spinRoY.setSingleStep(0.1)
        self.ui.spinRoY.setDecimals(3)
        self.ui.spinRoY.setValue(0)
        self.ui.spinRoY.setMaximum(360)
        self.ui.spinRoY.setMinimum(-360)
        self.ui.spinRoY.setMinimumWidth(30)

        self.ui.spinRoZ.setSingleStep(0.1)
        self.ui.spinRoZ.setDecimals(3)
        self.ui.spinRoZ.setValue(0)
        self.ui.spinRoZ.setMaximum(360)
        self.ui.spinRoZ.setMinimum(-360)
        self.ui.spinRoZ.setMinimumWidth(30)

        # --- Cấu hình các Spin Box cho Scale ---
        self.ui.spinScaX.setSingleStep(0.1)
        self.ui.spinScaX.setDecimals(3)
        self.ui.spinScaX.setValue(1)  # Giá trị scale mặc định thường là 1
        self.ui.spinScaX.setMaximum(10000)
        self.ui.spinScaX.setMinimum(0)
        self.ui.spinScaX.setMinimumWidth(30)

        self.ui.spinScaY.setSingleStep(0.1)
        self.ui.spinScaY.setDecimals(3)
        self.ui.spinScaY.setValue(1)  # Giá trị scale mặc định thường là 1
        self.ui.spinScaY.setMaximum(10000)
        self.ui.spinScaY.setMinimum(0)
        self.ui.spinScaY.setMinimumWidth(30)

        self.ui.spinScaZ.setSingleStep(0.1)
        self.ui.spinScaZ.setDecimals(3)
        self.ui.spinScaZ.setValue(1)  # Giá trị scale mặc định thường là 1
        self.ui.spinScaZ.setMaximum(10000)
        self.ui.spinScaZ.setMinimum(0)
        self.ui.spinScaZ.setMinimumWidth(30)


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
        self.ui.btnFAQs.clicked.connect(self.on_faqs)
        self.ui.btnGetPos.clicked.connect(self.getPosition)
        self.ui.btnSetPos.clicked.connect(self.setPosition)
        self.ui.btnStoreAll.clicked.connect(self.storeTransform_btn)
        self.ui.btnReStore.clicked.connect(self.restoreTransform_btn)

    # ============== SLOTS ==============
    # Các hàm này sẽ được gọi khi người dùng tương tác với giao diện.
    # Viết logic xử lý cho Maya vào đây.
    # ===================================


    def getPosition(self):

        selection = cmds.ls(selection=True, type='transform')
        if not selection:
            print("Vui lòng chọn một đối tượng để lấy thông số.")
            return
        # Sửa lỗi:
        # 1. Dùng self.ui.checkBox_Trans để truy cập widget.
        # 2. Dùng isChecked() không có tham số.
        # 3. Dùng self.ui.spin... để truy cập các spin box.
        if self.ui.checkBox_Trans.isChecked():
            translate = TransformFunction.getPosition()
            if translate:
                self.ui.spinPosX.setValue(translate[0])
                self.ui.spinPosY.setValue(translate[1])
                self.ui.spinPosZ.setValue(translate[2])


        if self.ui.checkBox_Rotate.isChecked():
            rotation = TransformFunction.getRotation()
            if rotation:
                self.ui.spinRoX.setValue(rotation[0])
                self.ui.spinRoY.setValue(rotation[1])
                self.ui.spinRoZ.setValue(rotation[2])

        if self.ui.checkBox_Scale.isChecked():
            scales = TransformFunction.getScale()
            if scales:
                self.ui.spinScaX.setValue(scales[0])
                self.ui.spinScaY.setValue(scales[1])
                self.ui.spinScaZ.setValue(scales[2])


    def setPosition(self):
        # Mở một chunk undo để người dùng có thể undo toàn bộ thao tác
        cmds.undoInfo(openChunk=True)
        try:
            # Kiểm tra checkbox Transform
            # Sửa lỗi: Thêm self.ui để truy cập widget và bỏ '== True' cho gọn
            if self.ui.checkBox_Trans.isChecked():
                # Sửa lỗi: Thêm self.ui để lấy giá trị từ spin box
                translateX = self.ui.spinPosX.value()
                translateY = self.ui.spinPosY.value()
                translateZ = self.ui.spinPosZ.value()

                # Gọi hàm set vị trí
                TransformFunction.setPosition([translateX, translateY, translateZ])

            # Kiểm tra checkbox Rotate
            if self.ui.checkBox_Rotate.isChecked():
                # Sửa lỗi: Thêm self.ui để lấy giá trị
                rotationX = self.ui.spinRoX.value()
                rotationY = self.ui.spinRoY.value()
                rotationZ = self.ui.spinRoZ.value()

                # Gọi hàm set xoay
                TransformFunction.setRotation([rotationX, rotationY, rotationZ])

            # Kiểm tra checkbox Scale
            if self.ui.checkBox_Scale.isChecked():
                # Sửa lỗi: Thêm self.ui để lấy giá trị
                scaleX = self.ui.spinScaX.value()
                scaleY = self.ui.spinScaY.value()
                scaleZ = self.ui.spinScaZ.value()

                # Gọi hàm set tỉ lệ
                TransformFunction.setScale([scaleX, scaleY, scaleZ])

            print('Set Position successfully')

        except Exception as e:
            # In ra lỗi nếu có sự cố xảy ra
            cmds.warning(f"Đã có lỗi xảy ra khi set vị trí: {e}")

        finally:
            # Luôn đóng chunk undo dù có lỗi hay không
            cmds.undoInfo(closeChunk=True)

    def storeTransform_btn(self):
        MeshPosTool.storeTransform()


    def restoreTransform_btn(self):
        MeshPosTool.restoreTransform()

    def on_faqs(self):
        cmds.confirmDialog(m=" Tool lấy thông tin Mesh "
                             "\n Store Transform lưu trữ toàn bộ thông tin của Scene, nên lưu trữ trước khi edit Scene"
                             "\n Có thắc mắc điều gì liên hệ ngay với HuangFei nhé")



def openWindow():
    # Lấy cửa sổ chính của Maya để làm parent
    mayaMainWindow = getMayaMainWindow()

    # Tìm xem đã có cửa sổ nào có objectName này chưa
    existingWindow = mayaMainWindow.findChild(QtWidgets.QWidget, "HF_MeshPositionTool_window")
    if existingWindow:
        existingWindow.close()
        existingWindow.deleteLater()

    # Tạo và hiển thị cửa sổ tool
    mainWin = HF_MeshPositionTool(parent=mayaMainWindow)
    mainWin.setObjectName("HF_MeshPositionTool_window")
    mainWin.show()
    return mainWin



openWindow()
