"""
Hoang Trong Phi
created 26/4/2024

"""
import maya.cmds as cmds
import maya.mel as mel


import sys
import os
import json

from maya import OpenMayaUI as omui
from select import select
try:
    from shiboken2 import wrapInstance

    from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide2.QtUiTools import QUiLoader
    from PySide2.QtCore import QFile, QIODevice
    from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide2.QtGui import QPixmap, QIcon
    from PySide2.QtCore import QObject, Qt
except:
    from shiboken6 import wrapInstance

    from PySide6 import QtUiTools, QtCore, QtGui, QtWidgets
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtCore import QFile, QIODevice
    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QPushButton
    from PySide6.QtGui import QPixmap, QIcon
    from PySide6.QtCore import QObject, Qt
from functools import partial

def getDirectoryofModule(modulename):

    #Input: module as string
    #OUtput:
        #List: name as string and directory of module

    module = modulename
    try:
        module = importlib.import_module(modulename)
    except:
        pass

    currWD = CommonPyFunction.Get_WD(module.__file__)
    return currWD
    pass


this_file_directory = os.path.dirname(__file__)
main_directory = os.path.dirname(this_file_directory)

data = os.path.dirname(this_file_directory) + r"\model\data"
UI_Path = os.path.dirname(this_file_directory) + r"\UI\Document.ui"

#####

class RG_Document(QtWidgets.QWidget):
    window = None  # đang rỗng

    def __init__(self, parent=None):
        """
        Initialize class.

        """
        #initialize window and load UI file
        super(RG_Document, self).__init__(parent=parent)
        ##

        self.createWidgets()
        self.createConnection()


    def createWidgets(self):

        self.checkerBoxOpt = QtWidgets.QAbstractButton
        self.setWindowFlags(QtCore.Qt.Window)
        self.widget = QtUiTools.QUiLoader().load(UI_Path)
        self.widget.setParent(self)
            # set initial window size
        self.setFixedSize(380, 780)

        # set intial button
        #### Note: dat ten bien trung voi objectName de tien quan ly,
        ####  -> nhung doi khi de gay conflict trong qua trinh doc lai

        ### Indie_Rigger button
        self.btn_Rename = self.widget.findChild( QtWidgets.QPushButton, "btn_Rename")
        self.btn_Rename_Guide = self.widget.findChild( QtWidgets.QPushButton, "btn_Rename_Guide")
        self.btn_Rename_ytb   = self.widget.findChild( QtWidgets.QPushButton, "btn_Rename_ytb")

        self.btn_Joint = self.widget.findChild( QtWidgets.QPushButton, "btn_Joint")
        self.btn_Joint_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_Joint_Guide")
        self.btn_Joint_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_Joint_ytb")
        
        self.btn_Controller = self.widget.findChild( QtWidgets.QPushButton, "btn_Controller")
        self.btn_Controller_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_Controller_Guide")
        self.btn_Controller_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_Controller_ytb")

        self.btn_CustomColor = self.widget.findChild(QtWidgets.QPushButton, "btn_CustomColor")
        self.btn_CustomColor_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_CustomColor_Guide")
        self.btn_CustomColor_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_CustomColor_ytb")

        self.btn_BlendShape = self.widget.findChild(QtWidgets.QPushButton, "btn_BlendShape")
        self.btn_BlendShape_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_BlendShape_Guide")
        self.btn_BlendShape_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_BlendShape_ytb")


        ### Anim Bai button
        self.btn_SkinMagic = self.widget.findChild(QtWidgets.QPushButton, "btn_SkinMagic")
        self.btn_SkinMagic_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_SkinMagic_Guide")
        self.btn_SkinMagic_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_SkinMagic_ytb")

        self.btn_SpringMagic = self.widget.findChild(QtWidgets.QPushButton, "btn_SpringMagic")
        self.btn_SpringMagic_Guide = self.widget.findChild(QtWidgets.QPushButton, "btn_SpringMagic_Guide")
        self.btn_SpringMagic_ytb = self.widget.findChild(QtWidgets.QPushButton, "btn_SpringMagic_ytb")


        ### RG_Modeling  button
        self.btn_BakingToolsets = self.widget.findChild(QtWidgets.QPushButton, "btn_BakingToolsets")
        self.btn_ScaleManReference = self.widget.findChild(QtWidgets.QPushButton, "btn_ScaleManReference")
        self.btn_PivotTool = self.widget.findChild(QtWidgets.QPushButton, "btn_PivotTool")
        self.btn_UV = self.widget.findChild(QtWidgets.QPushButton, "btn_UV")
        self.btn_CleanUpTool = self.widget.findChild(QtWidgets.QPushButton, "btn_CleanUpTool")
        self.btn_FixTool = self.widget.findChild(QtWidgets.QPushButton, "btn_FixTool")


        ### RG_Another
        self.btn_ComingSoon = self.widget.findChild(QtWidgets.QPushButton, "btn_ComingSoon")

        # Assign functionally to buttons
    def createConnection(self):
        #Your code goes here
        
        ### Indie_Rigger button   ,bug clicked
        try:
            self.btn_Rename.clicked.connect(self.demoReNameButton)
            self.btn_Rename_Guide.clicked.connect(self.demoReNameButton)
            self.btn_Rename_ytb.clicked.connect(self.demoReNameButton)
            
            self.btn_Joint.clicked.connect(self.demoReNameButton)
            self.btn_Joint_Guide.clicked.connect(self.demoReNameButton)
            self.btn_Joint_ytb.clicked.connect(self.demoReNameButton)
            
            self.btn_Controller.clicked.connect(self.demoReNameButton)
            self.btn_Controller_Guide.clicked.connect(self.demoReNameButton)
            self.btn_Controller_ytb.clicked.connect(self.demoReNameButton)
            
            self.btn_CustomColor.clicked.connect(self.demoReNameButton)
            self.btn_CustomColor_Guide.clicked.connect(self.demoReNameButton)
            self.btn_CustomColor_ytb.clicked.connect(self.demoReNameButton)
            
            self.btn_BlendShape.clicked.connect(self.demoReNameButton)
            self.btn_BlendShape_Guide.clicked.connect(self.demoReNameButton)
            self.btn_BlendShape_ytb.clicked.connect(self.demoReNameButton)


            #### Anim Bai
            self.btn_SkinMagic.clicked.connect(self.demoReNameButton)
            self.btn_SkinMagic_Guide.clicked.connect(self.demoReNameButton)
            self.btn_SkinMagic_ytb.clicked.connect(self.demoReNameButton)

            self.btn_SpringMagic.clicked.connect(self.demoReNameButton)
            self.btn_SpringMagic_Guide.clicked.connect(self.demoReNameButton)
            self.btn_SpringMagic_ytb.clicked.connect(self.demoReNameButton)

            ### RG_Modeling  button
            self.btn_BakingToolsets.clicked.connect(self.demoReNameButton)
            self.btn_ScaleManReference.clicked.connect(self.demoReNameButton)
            self.btn_PivotTool.clicked.connect(self.demoReNameButton)
            self.btn_UV.clicked.connect(self.demoReNameButton)
            self.btn_CleanUpTool.clicked.connect(self.demoReNameButton)
            self.btn_ComingSoon.clicked.connect(self.demoReNameButton)

            ### RG_Another
            self.btn_ComingSoon.clicked.connect(self.ComingSoon)

        except:
            pass
            
        #
       
        
    def demoReNameButton(self):
        print ("Button Da kich hoat" )


    def SmartJointBtn(self):
        print("Smart Joint Da kich ")

    def ComingSoon(self):
        cmds.confirmDialog(title='Warining', message='Tab này sẽ được Cập nhật sau', )



def openWindow():  # Create UI

    """
    ID Maya and attach tool window.
    """

    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in QtWidgets.QApplication.allWindows():
        #for win in QtWidgets.QApplication.allWindows():
            if "mainWindow" in win.objectName():
                win.destroy()

    # QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    RG_Document.window = RG_Document(parent=mayaMainWindow)
    RG_Document.window.setObjectName("mainWindow")
    RG_Document.window.setWindowTitle("RG Document")
    RG_Document.window.show()

openWindow()


