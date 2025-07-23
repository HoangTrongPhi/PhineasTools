# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BakeTool.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
QWidget = QtWidgets.QWidget
QLabel = QtWidgets.QLabel
QPushButton = QtWidgets.QPushButton
QFrame = QtWidgets.QFrame
QRect = QtCore.QRect
QFont = QtGui.QFont
QCoreApplication = QtCore.QCoreApplication
QMenuBar = QtWidgets.QMenuBar
QStatusBar = QtWidgets.QStatusBar
QDoubleSpinBox = QtWidgets.QDoubleSpinBox
QTextEdit = QtWidgets.QTextEdit
QMetaObject = QtCore.QMetaObject
QSizePolicy = QtWidgets.QSizePolicy

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(410, 620)
        mainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.RG_author = QLabel(self.centralwidget)
        self.RG_author.setObjectName(u"RG_author")
        self.RG_author.setGeometry(QRect(12, 543, 66, 16))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.RG_author.setFont(font)
        self.RG_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:9pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_Display = QLabel(self.centralwidget)
        self.label_Display.setObjectName(u"label_Display")
        self.label_Display.setGeometry(QRect(10, 191, 102, 20))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(False)
        self.label_Display.setFont(font1)
        self.label_Display.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnFAQs_all = QPushButton(self.centralwidget)
        self.btnFAQs_all.setObjectName(u"btnFAQs_all")
        self.btnFAQs_all.setGeometry(QRect(380, 10, 25, 23))
        self.btnBakeSet = QPushButton(self.centralwidget)
        self.btnBakeSet.setObjectName(u"btnBakeSet")
        self.btnBakeSet.setGeometry(QRect(13, 100, 386, 64))
        self.btnBakeSet.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExportHigh = QPushButton(self.centralwidget)
        self.btnExportHigh.setObjectName(u"btnExportHigh")
        self.btnExportHigh.setGeometry(QRect(4, 448, 100, 36))
        self.btnExportHigh.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnDisHigh = QPushButton(self.centralwidget)
        self.btnDisHigh.setObjectName(u"btnDisHigh")
        self.btnDisHigh.setGeometry(QRect(10, 212, 80, 30))
        self.btnDisHigh.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(6, 321, 400, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnDisLow = QPushButton(self.centralwidget)
        self.btnDisLow.setObjectName(u"btnDisLow")
        self.btnDisLow.setGeometry(QRect(92, 212, 80, 30))
        self.btnDisLow.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;;\n"
"}\n"
"")
        self.label_Export = QLabel(self.centralwidget)
        self.label_Export.setObjectName(u"label_Export")
        self.label_Export.setGeometry(QRect(10, 420, 68, 20))
        self.label_Export.setFont(font1)
        self.label_Export.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnDisReset = QPushButton(self.centralwidget)
        self.btnDisReset.setObjectName(u"btnDisReset")
        self.btnDisReset.setGeometry(QRect(215, 287, 100, 32))
        self.btnDisReset.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.btnDisSwap = QPushButton(self.centralwidget)
        self.btnDisSwap.setObjectName(u"btnDisSwap")
        self.btnDisSwap.setGeometry(QRect(174, 212, 226, 30))
        self.btnDisSwap.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.btnExportLow = QPushButton(self.centralwidget)
        self.btnExportLow.setObjectName(u"btnExportLow")
        self.btnExportLow.setGeometry(QRect(107, 448, 100, 36))
        self.btnExportLow.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnExportAll = QPushButton(self.centralwidget)
        self.btnExportAll.setObjectName(u"btnExportAll")
        self.btnExportAll.setGeometry(QRect(210, 448, 189, 36))
        self.btnExportAll.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 400, 400, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.btnExportExplore = QPushButton(self.centralwidget)
        self.btnExportExplore.setObjectName(u"btnExportExplore")
        self.btnExportExplore.setGeometry(QRect(10, 490, 36, 36))
        self.btnExportExplore.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_Selection = QLabel(self.centralwidget)
        self.label_Selection.setObjectName(u"label_Selection")
        self.label_Selection.setGeometry(QRect(10, 332, 91, 20))
        self.label_Selection.setFont(font1)
        self.label_Selection.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnDisExplode = QPushButton(self.centralwidget)
        self.btnDisExplode.setObjectName(u"btnDisExplode")
        self.btnDisExplode.setGeometry(QRect(93, 287, 120, 32))
        self.btnDisExplode.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 4px;\n"
"}\n"
"")
        self.btnSelectHigh = QPushButton(self.centralwidget)
        self.btnSelectHigh.setObjectName(u"btnSelectHigh")
        self.btnSelectHigh.setGeometry(QRect(10, 361, 80, 30))
        self.btnSelectHigh.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnSelectLow = QPushButton(self.centralwidget)
        self.btnSelectLow.setObjectName(u"btnSelectLow")
        self.btnSelectLow.setGeometry(QRect(92, 361, 80, 30))
        self.btnSelectLow.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnSelectPair = QPushButton(self.centralwidget)
        self.btnSelectPair.setObjectName(u"btnSelectPair")
        self.btnSelectPair.setGeometry(QRect(173, 361, 80, 30))
        self.btnSelectPair.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnFAQs_select = QPushButton(self.centralwidget)
        self.btnFAQs_select.setObjectName(u"btnFAQs_select")
        self.btnFAQs_select.setGeometry(QRect(378, 332, 25, 23))
        self.btnFAQs_display = QPushButton(self.centralwidget)
        self.btnFAQs_display.setObjectName(u"btnFAQs_display")
        self.btnFAQs_display.setGeometry(QRect(378, 187, 25, 23))
        self.label_SetCreate = QLabel(self.centralwidget)
        self.label_SetCreate.setObjectName(u"label_SetCreate")
        self.label_SetCreate.setGeometry(QRect(10, 51, 133, 20))
        self.label_SetCreate.setFont(font1)
        self.label_SetCreate.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.label_SetTips = QLabel(self.centralwidget)
        self.label_SetTips.setObjectName(u"label_SetTips")
        self.label_SetTips.setGeometry(QRect(10, 71, 204, 20))
        self.label_SetTips.setFont(font1)
        self.label_SetTips.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.label_Warning = QLabel(self.centralwidget)
        self.label_Warning.setObjectName(u"label_Warning")
        self.label_Warning.setGeometry(QRect(10, 10, 327, 29))
        self.label_Warning.setFont(font1)
        self.label_Warning.setStyleSheet(u"color: rgb(255, 180, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnExportSpecial = QPushButton(self.centralwidget)
        self.btnExportSpecial.setObjectName(u"btnExportSpecial")
        self.btnExportSpecial.setGeometry(QRect(276, 491, 124, 36))
        self.btnExportSpecial.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.btnFAQs_export = QPushButton(self.centralwidget)
        self.btnFAQs_export.setObjectName(u"btnFAQs_export")
        self.btnFAQs_export.setGeometry(QRect(378, 420, 25, 23))
        self.spinBoxDis = QDoubleSpinBox(self.centralwidget)
        self.spinBoxDis.setObjectName(u"spinBoxDis")
        self.spinBoxDis.setGeometry(QRect(10, 285, 80, 36))
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 171, 400, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_Warning_2 = QLabel(self.centralwidget)
        self.label_Warning_2.setObjectName(u"label_Warning_2")
        self.label_Warning_2.setGeometry(QRect(10, 251, 327, 29))
        self.label_Warning_2.setFont(font1)
        self.label_Warning_2.setStyleSheet(u"color: rgb(255, 180, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnSelectSmallToBig = QPushButton(self.centralwidget)
        self.btnSelectSmallToBig.setObjectName(u"btnSelectSmallToBig")
        self.btnSelectSmallToBig.setGeometry(QRect(340, 361, 60, 30))
        self.btnSelectSmallToBig.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.label_Warning_3 = QLabel(self.centralwidget)
        self.label_Warning_3.setObjectName(u"label_Warning_3")
        self.label_Warning_3.setGeometry(QRect(77, 419, 166, 21))
        self.label_Warning_3.setFont(font1)
        self.label_Warning_3.setStyleSheet(u"color: rgb(255, 180, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btnSelectBigToSmall = QPushButton(self.centralwidget)
        self.btnSelectBigToSmall.setObjectName(u"btnSelectBigToSmall")
        self.btnSelectBigToSmall.setGeometry(QRect(278, 361, 60, 30))
        self.btnSelectBigToSmall.setStyleSheet(u"QPushButton {\n"
"font:12pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
" }\n"
"QPushButton:hover{\n"
"background-color:  rgb(125, 125, 125);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
"}\n"
"")
        self.textEditPath = QTextEdit(self.centralwidget)
        self.textEditPath.setObjectName(u"textEditPath")
        self.textEditPath.setGeometry(QRect(50, 491, 220, 36))
        mainWindow.setCentralWidget(self.centralwidget)
        self.RG_author.raise_()
        self.label_Display.raise_()
        self.btnFAQs_all.raise_()
        self.btnBakeSet.raise_()
        self.btnExportHigh.raise_()
        self.line.raise_()
        self.btnDisLow.raise_()
        self.label_Export.raise_()
        self.btnDisReset.raise_()
        self.btnDisSwap.raise_()
        self.btnExportLow.raise_()
        self.btnExportAll.raise_()
        self.line_2.raise_()
        self.btnExportExplore.raise_()
        self.label_Selection.raise_()
        self.btnDisExplode.raise_()
        self.btnSelectHigh.raise_()
        self.btnSelectLow.raise_()
        self.btnSelectPair.raise_()
        self.btnFAQs_select.raise_()
        self.btnFAQs_display.raise_()
        self.label_SetCreate.raise_()
        self.label_SetTips.raise_()
        self.label_Warning.raise_()
        self.btnExportSpecial.raise_()
        self.btnDisHigh.raise_()
        self.btnFAQs_export.raise_()
        self.spinBoxDis.raise_()
        self.line_3.raise_()
        self.label_Warning_2.raise_()
        self.btnSelectSmallToBig.raise_()
        self.label_Warning_3.raise_()
        self.btnSelectBigToSmall.raise_()
        self.textEditPath.raise_()
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 410, 33))
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
        self.label_Display.setText(QCoreApplication.translate("mainWindow", u"DISPLAY TOGGLE", None))
        self.btnFAQs_all.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnBakeSet.setText(QCoreApplication.translate("mainWindow", u"Create BakeSet", None))
        self.btnExportHigh.setText(QCoreApplication.translate("mainWindow", u"Export High", None))
        self.btnDisHigh.setText(QCoreApplication.translate("mainWindow", u"High", None))
        self.btnDisLow.setText(QCoreApplication.translate("mainWindow", u"Low", None))
        self.label_Export.setText(QCoreApplication.translate("mainWindow", u"EXPORT", None))
        self.btnDisReset.setText(QCoreApplication.translate("mainWindow", u"Reset", None))
        self.btnDisSwap.setText(QCoreApplication.translate("mainWindow", u"Swap", None))
        self.btnExportLow.setText(QCoreApplication.translate("mainWindow", u"Export Low", None))
        self.btnExportAll.setText(QCoreApplication.translate("mainWindow", u"All Export --> 1FBX", None))
        self.btnExportExplore.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.label_Selection.setText(QCoreApplication.translate("mainWindow", u"SELECTION", None))
        self.btnDisExplode.setText(QCoreApplication.translate("mainWindow", u"Explode", None))
        self.btnSelectHigh.setText(QCoreApplication.translate("mainWindow", u"High", None))
        self.btnSelectLow.setText(QCoreApplication.translate("mainWindow", u"Low", None))
        self.btnSelectPair.setText(QCoreApplication.translate("mainWindow", u"Pair", None))
        self.btnFAQs_select.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btnFAQs_display.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.label_SetCreate.setText(QCoreApplication.translate("mainWindow", u"SETUP & CREATE", None))
        self.label_SetTips.setText(QCoreApplication.translate("mainWindow", u"Ch\u1ecdn m\u1ed9t c\u1eb7p ( pair) mesh v\u00e0 click", None))
        self.label_Warning.setText(QCoreApplication.translate("mainWindow", u" Warning: V\u1edbi tr\u01b0\u1eddng h\u1ee3p d\u00f9ng nhi\u1ec1u texture set\n"
" C\u1ea7n assign material tr\u01b0\u1edbc r\u1ed3i h\u00e3y l\u00e0m bakeset", None))
        self.btnExportSpecial.setText(QCoreApplication.translate("mainWindow", u"EXPORT", None))
        self.btnFAQs_export.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.label_Warning_2.setText(QCoreApplication.translate("mainWindow", u"Bung t\u1eebng c\u1eb7p Mesh Low/High tr\u00e1nh bake b\u1ecb lem map", None))
        self.btnSelectSmallToBig.setText(QCoreApplication.translate("mainWindow", u">>>", None))
        self.label_Warning_3.setText(QCoreApplication.translate("mainWindow", u" Export theo Scene \u0111\u00e3 save", None))
        self.btnSelectBigToSmall.setText(QCoreApplication.translate("mainWindow", u"<<<", None))
    # retranslateUi

