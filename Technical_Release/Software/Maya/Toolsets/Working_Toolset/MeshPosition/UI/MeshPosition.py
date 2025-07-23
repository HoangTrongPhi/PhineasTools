# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MeshPosition.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################



#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
QWidget = QtWidgets.QWidget
QFrame = QtWidgets.QFrame
QLabel = QtWidgets.QLabel
QDoubleSpinBox = QtWidgets.QDoubleSpinBox
QCheckBox = QtWidgets.QCheckBox
QPushButton = QtWidgets.QPushButton
QMenuBar = QtWidgets.QMenuBar
QStatusBar = QtWidgets.QStatusBar
QCoreApplication = QtCore.QCoreApplication
QRect = QtCore.QRect
QFont = QtGui.QFont
QMetaObject = QtCore.QMetaObject
QSizePolicy = QtWidgets.QSizePolicy

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(460, 310)
        mainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RG_author = QLabel(self.centralwidget)
        self.RG_author.setObjectName(u"RG_author")
        self.RG_author.setGeometry(QRect(12, 250, 59, 16))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.RG_author.setFont(font)
        self.RG_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:9pt \"Bahnschrift SemiBold SemiConden\";")
        self.RG_label_1 = QLabel(self.centralwidget)
        self.RG_label_1.setObjectName(u"RG_label_1")
        self.RG_label_1.setGeometry(QRect(14, 11, 422, 20))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(False)
        self.RG_label_1.setFont(font1)
        self.RG_label_1.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:12pt  \"Bahnschrift SemiBold SemiConden\";")
        self.spinPosX = QDoubleSpinBox(self.centralwidget)
        self.spinPosX.setObjectName(u"spinPosX")
        self.spinPosX.setGeometry(QRect(100, 50, 110, 22))
        self.spinPosX.setDecimals(3)
        self.spinPosY = QDoubleSpinBox(self.centralwidget)
        self.spinPosY.setObjectName(u"spinPosY")
        self.spinPosY.setGeometry(QRect(220, 50, 110, 22))
        self.spinPosY.setDecimals(3)
        self.spinPosZ = QDoubleSpinBox(self.centralwidget)
        self.spinPosZ.setObjectName(u"spinPosZ")
        self.spinPosZ.setGeometry(QRect(340, 50, 110, 22))
        self.spinPosZ.setDecimals(3)
        self.spinRoX = QDoubleSpinBox(self.centralwidget)
        self.spinRoX.setObjectName(u"spinRoX")
        self.spinRoX.setGeometry(QRect(100, 80, 110, 22))
        self.spinRoX.setDecimals(3)
        self.spinRoY = QDoubleSpinBox(self.centralwidget)
        self.spinRoY.setObjectName(u"spinRoY")
        self.spinRoY.setGeometry(QRect(220, 80, 110, 22))
        self.spinRoY.setDecimals(3)
        self.spinRoZ = QDoubleSpinBox(self.centralwidget)
        self.spinRoZ.setObjectName(u"spinRoZ")
        self.spinRoZ.setGeometry(QRect(340, 80, 110, 22))
        self.spinRoZ.setDecimals(3)
        self.checkBox_Trans = QCheckBox(self.centralwidget)
        self.checkBox_Trans.setObjectName(u"checkBox_Trans")
        self.checkBox_Trans.setGeometry(QRect(10, 46, 80, 30))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font2.setPointSize(10)
        self.checkBox_Trans.setFont(font2)
        self.checkBox_Trans.setChecked(False)
        self.checkBox_Rotate = QCheckBox(self.centralwidget)
        self.checkBox_Rotate.setObjectName(u"checkBox_Rotate")
        self.checkBox_Rotate.setGeometry(QRect(10, 80, 80, 16))
        self.checkBox_Rotate.setFont(font2)
        self.checkBox_Scale = QCheckBox(self.centralwidget)
        self.checkBox_Scale.setObjectName(u"checkBox_Scale")
        self.checkBox_Scale.setGeometry(QRect(10, 110, 100, 16))
        self.checkBox_Scale.setFont(font2)
        self.spinScaX = QDoubleSpinBox(self.centralwidget)
        self.spinScaX.setObjectName(u"spinScaX")
        self.spinScaX.setGeometry(QRect(100, 110, 110, 22))
        self.spinScaX.setDecimals(3)
        self.spinScaZ = QDoubleSpinBox(self.centralwidget)
        self.spinScaZ.setObjectName(u"spinScaZ")
        self.spinScaZ.setGeometry(QRect(340, 110, 110, 22))
        self.spinScaZ.setDecimals(3)
        self.spinScaY = QDoubleSpinBox(self.centralwidget)
        self.spinScaY.setObjectName(u"spinScaY")
        self.spinScaY.setGeometry(QRect(220, 110, 110, 22))
        self.spinScaY.setDecimals(3)
        self.btnFAQs = QPushButton(self.centralwidget)
        self.btnFAQs.setObjectName(u"btnFAQs")
        self.btnFAQs.setGeometry(QRect(431, 10, 25, 23))
        self.btnGetPos = QPushButton(self.centralwidget)
        self.btnGetPos.setObjectName(u"btnGetPos")
        self.btnGetPos.setGeometry(QRect(12, 140, 210, 35))
        self.btnGetPos.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnSetPos = QPushButton(self.centralwidget)
        self.btnSetPos.setObjectName(u"btnSetPos")
        self.btnSetPos.setGeometry(QRect(240, 140, 210, 35))
        self.btnSetPos.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnStoreAll = QPushButton(self.centralwidget)
        self.btnStoreAll.setObjectName(u"btnStoreAll")
        self.btnStoreAll.setGeometry(QRect(12, 210, 210, 35))
        self.btnStoreAll.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btnReStore = QPushButton(self.centralwidget)
        self.btnReStore.setObjectName(u"btnReStore")
        self.btnReStore.setGeometry(QRect(240, 210, 210, 35))
        self.btnReStore.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 190, 440, 3))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 21))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.RG_author.setText(QCoreApplication.translate("mainWindow", u"@HuangFei", None))
        self.RG_label_1.setText(QCoreApplication.translate("mainWindow", u"Copy Transform Position:", None))
        self.checkBox_Trans.setText(QCoreApplication.translate("mainWindow", u"Transform", None))
        self.checkBox_Rotate.setText(QCoreApplication.translate("mainWindow", u"Rotate", None))
        self.checkBox_Scale.setText(QCoreApplication.translate("mainWindow", u"Scale", None))
        self.btnFAQs.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnGetPos.setText(QCoreApplication.translate("mainWindow", u"Get Position", None))
        self.btnSetPos.setText(QCoreApplication.translate("mainWindow", u"Set Position", None))
        self.btnStoreAll.setText(QCoreApplication.translate("mainWindow", u"Store Transfrom All Scene", None))
        self.btnReStore.setText(QCoreApplication.translate("mainWindow", u"ReStore Transform", None))
    # retranslateUi

