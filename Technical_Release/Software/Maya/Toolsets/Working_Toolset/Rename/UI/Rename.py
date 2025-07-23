# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Rename.ui'
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
QDoubleSpinBox = QtWidgets.QDoubleSpinBox
QCheckBox = QtWidgets.QCheckBox
QTextEdit = QtWidgets.QTextEdit
QFrame = QtWidgets.QFrame
QRect = QtCore.QRect
QFont = QtGui.QFont
QMenuBar = QtWidgets.QMenuBar
QStatusBar = QtWidgets.QStatusBar
QCoreApplication = QtCore.QCoreApplication
QMetaObject = QtCore.QMetaObject

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(380, 780)
        mainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_author = QLabel(self.centralwidget)
        self.lbl_author.setObjectName(u"lbl_author")
        self.lbl_author.setGeometry(QRect(12, 694, 68, 16))
        font = QFont()
        font.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.lbl_author.setFont(font)
        self.lbl_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:9pt \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Rename = QLabel(self.centralwidget)
        self.lbl_Rename.setObjectName(u"lbl_Rename")
        self.lbl_Rename.setGeometry(QRect(12, 6, 113, 20))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(False)
        self.lbl_Rename.setFont(font1)
        self.lbl_Rename.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:12pt  \"Bahnschrift SemiBold SemiConden\";")
        self.dsb_Start = QDoubleSpinBox(self.centralwidget)
        self.dsb_Start.setObjectName(u"dsb_Start")
        self.dsb_Start.setGeometry(QRect(63, 72, 80, 20))
        self.dsb_Start.setDecimals(3)
        self.chkb_Hierachy = QCheckBox(self.centralwidget)
        self.chkb_Hierachy.setObjectName(u"chkb_Hierachy")
        self.chkb_Hierachy.setGeometry(QRect(14, 504, 80, 24))
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light SemiCondensed"])
        font2.setPointSize(10)
        self.chkb_Hierachy.setFont(font2)
        self.chkb_Hierachy.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.chkb_Hierachy.setChecked(False)
        self.chkb_Selected = QCheckBox(self.centralwidget)
        self.chkb_Selected.setObjectName(u"chkb_Selected")
        self.chkb_Selected.setGeometry(QRect(144, 504, 80, 24))
        self.chkb_Selected.setFont(font2)
        self.chkb_Selected.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.chkb_All = QCheckBox(self.centralwidget)
        self.chkb_All.setObjectName(u"chkb_All")
        self.chkb_All.setGeometry(QRect(284, 504, 80, 24))
        self.chkb_All.setFont(font2)
        self.chkb_All.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.btn_reNum = QPushButton(self.centralwidget)
        self.btn_reNum.setObjectName(u"btn_reNum")
        self.btn_reNum.setGeometry(QRect(9, 102, 360, 36))
        self.btn_reNum.setStyleSheet(u"QPushButton {\n"
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
        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(10, 271, 360, 16))
        self.line_1.setFrameShape(QFrame.Shape.HLine)
        self.line_1.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_FirstChar = QPushButton(self.centralwidget)
        self.btn_FirstChar.setObjectName(u"btn_FirstChar")
        self.btn_FirstChar.setGeometry(QRect(10, 221, 160, 36))
        self.btn_FirstChar.setStyleSheet(u"QPushButton {\n"
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
        self.btn_LastChar = QPushButton(self.centralwidget)
        self.btn_LastChar.setObjectName(u"btn_LastChar")
        self.btn_LastChar.setGeometry(QRect(210, 221, 160, 36))
        self.btn_LastChar.setStyleSheet(u"QPushButton {\n"
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
        self.txt_HashRename = QTextEdit(self.centralwidget)
        self.txt_HashRename.setObjectName(u"txt_HashRename")
        self.txt_HashRename.setGeometry(QRect(10, 317, 280, 30))
        self.txt_AddBefore = QTextEdit(self.centralwidget)
        self.txt_AddBefore.setObjectName(u"txt_AddBefore")
        self.txt_AddBefore.setGeometry(QRect(67, 143, 220, 30))
        self.txt_Rename = QTextEdit(self.centralwidget)
        self.txt_Rename.setObjectName(u"txt_Rename")
        self.txt_Rename.setGeometry(QRect(8, 37, 360, 30))
        self.lbl_Start = QLabel(self.centralwidget)
        self.lbl_Start.setObjectName(u"lbl_Start")
        self.lbl_Start.setGeometry(QRect(11, 74, 49, 16))
        self.lbl_Start.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.dsb_Padding = QDoubleSpinBox(self.centralwidget)
        self.dsb_Padding.setObjectName(u"dsb_Padding")
        self.dsb_Padding.setGeometry(QRect(287, 72, 80, 20))
        self.dsb_Padding.setDecimals(3)
        self.lbl_Padding = QLabel(self.centralwidget)
        self.lbl_Padding.setObjectName(u"lbl_Padding")
        self.lbl_Padding.setGeometry(QRect(227, 73, 49, 16))
        self.lbl_Padding.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.lbl_HashRename = QLabel(self.centralwidget)
        self.lbl_HashRename.setObjectName(u"lbl_HashRename")
        self.lbl_HashRename.setGeometry(QRect(12, 287, 130, 20))
        self.lbl_HashRename.setFont(font1)
        self.lbl_HashRename.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:12pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btn_Rename = QPushButton(self.centralwidget)
        self.btn_Rename.setObjectName(u"btn_Rename")
        self.btn_Rename.setGeometry(QRect(295, 311, 74, 36))
        self.btn_Rename.setStyleSheet(u"QPushButton {\n"
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
        self.txt_AddAfter = QTextEdit(self.centralwidget)
        self.txt_AddAfter.setObjectName(u"txt_AddAfter")
        self.txt_AddAfter.setGeometry(QRect(67, 181, 220, 30))
        self.lbl_Before = QLabel(self.centralwidget)
        self.lbl_Before.setObjectName(u"lbl_Before")
        self.lbl_Before.setGeometry(QRect(12, 147, 53, 20))
        font3 = QFont()
        font3.setFamilies([u"Bahnschrift SemiBold SemiConden"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(False)
        self.lbl_Before.setFont(font3)
        self.lbl_Before.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_After = QLabel(self.centralwidget)
        self.lbl_After.setObjectName(u"lbl_After")
        self.lbl_After.setGeometry(QRect(12, 185, 53, 20))
        self.lbl_After.setFont(font3)
        self.lbl_After.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btn_addBefore = QPushButton(self.centralwidget)
        self.btn_addBefore.setObjectName(u"btn_addBefore")
        self.btn_addBefore.setGeometry(QRect(293, 142, 74, 30))
        self.btn_addBefore.setStyleSheet(u"QPushButton {\n"
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
        self.btn_addAfter = QPushButton(self.centralwidget)
        self.btn_addAfter.setObjectName(u"btn_addAfter")
        self.btn_addAfter.setGeometry(QRect(294, 180, 74, 30))
        self.btn_addAfter.setStyleSheet(u"QPushButton {\n"
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
        self.txt_Search = QTextEdit(self.centralwidget)
        self.txt_Search.setObjectName(u"txt_Search")
        self.txt_Search.setGeometry(QRect(10, 416, 270, 30))
        self.txt_Replace = QTextEdit(self.centralwidget)
        self.txt_Replace.setObjectName(u"txt_Replace")
        self.txt_Replace.setGeometry(QRect(10, 470, 270, 30))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(11, 357, 360, 16))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_Search = QLabel(self.centralwidget)
        self.lbl_Search.setObjectName(u"lbl_Search")
        self.lbl_Search.setGeometry(QRect(11, 393, 53, 20))
        self.lbl_Search.setFont(font3)
        self.lbl_Search.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Replace = QLabel(self.centralwidget)
        self.lbl_Replace.setObjectName(u"lbl_Replace")
        self.lbl_Replace.setGeometry(QRect(13, 449, 53, 20))
        self.lbl_Replace.setFont(font3)
        self.lbl_Replace.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 535, 360, 16))
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_Pre_01 = QPushButton(self.centralwidget)
        self.btn_Pre_01.setObjectName(u"btn_Pre_01")
        self.btn_Pre_01.setGeometry(QRect(10, 581, 56, 30))
        self.btn_Pre_01.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.btn_Pre_02 = QPushButton(self.centralwidget)
        self.btn_Pre_02.setObjectName(u"btn_Pre_02")
        self.btn_Pre_02.setGeometry(QRect(70, 581, 56, 30))
        self.btn_Pre_02.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.btn_Pre_03 = QPushButton(self.centralwidget)
        self.btn_Pre_03.setObjectName(u"btn_Pre_03")
        self.btn_Pre_03.setGeometry(QRect(131, 580, 56, 30))
        self.btn_Pre_03.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.btn_Pre_04 = QPushButton(self.centralwidget)
        self.btn_Pre_04.setObjectName(u"btn_Pre_04")
        self.btn_Pre_04.setGeometry(QRect(191, 580, 56, 30))
        self.btn_Pre_04.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.btn_Pre_05 = QPushButton(self.centralwidget)
        self.btn_Pre_05.setObjectName(u"btn_Pre_05")
        self.btn_Pre_05.setGeometry(QRect(251, 580, 56, 30))
        self.btn_Pre_05.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.btn_Pre_06 = QPushButton(self.centralwidget)
        self.btn_Pre_06.setObjectName(u"btn_Pre_06")
        self.btn_Pre_06.setGeometry(QRect(311, 580, 56, 30))
        self.btn_Pre_06.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        self.lbl_Prefix = QLabel(self.centralwidget)
        self.lbl_Prefix.setObjectName(u"lbl_Prefix")
        self.lbl_Prefix.setGeometry(QRect(13, 560, 53, 16))
        self.lbl_Prefix.setFont(font3)
        self.lbl_Prefix.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Package = QLabel(self.centralwidget)
        self.lbl_Package.setObjectName(u"lbl_Package")
        self.lbl_Package.setGeometry(QRect(13, 621, 54, 20))
        self.lbl_Package.setFont(font3)
        self.lbl_Package.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.btn_FAQsAll = QPushButton(self.centralwidget)
        self.btn_FAQsAll.setObjectName(u"btn_FAQsAll")
        self.btn_FAQsAll.setGeometry(QRect(338, 6, 25, 23))
        self.btn_FAQsAll.setStyleSheet(u"")
        self.btn_FAQsSearch = QPushButton(self.centralwidget)
        self.btn_FAQsSearch.setObjectName(u"btn_FAQsSearch")
        self.btn_FAQsSearch.setGeometry(QRect(341, 388, 25, 23))
        self.btn_FAQsAddPrefix = QPushButton(self.centralwidget)
        self.btn_FAQsAddPrefix.setObjectName(u"btn_FAQsAddPrefix")
        self.btn_FAQsAddPrefix.setGeometry(QRect(338, 549, 25, 23))
        self.btn_pkgSort = QPushButton(self.centralwidget)
        self.btn_pkgSort.setObjectName(u"btn_pkgSort")
        self.btn_pkgSort.setGeometry(QRect(87, 616, 280, 30))
        self.btn_pkgSort.setStyleSheet(u"QPushButton {\n"
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
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btn_pkgCleanGroup = QPushButton(self.centralwidget)
        self.btn_pkgCleanGroup.setObjectName(u"btn_pkgCleanGroup")
        self.btn_pkgCleanGroup.setGeometry(QRect(10, 656, 168, 30))
        self.btn_pkgCleanGroup.setStyleSheet(u"QPushButton {\n"
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
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btn_pkgReset = QPushButton(self.centralwidget)
        self.btn_pkgReset.setObjectName(u"btn_pkgReset")
        self.btn_pkgReset.setGeometry(QRect(187, 656, 181, 30))
        self.btn_pkgReset.setStyleSheet(u"QPushButton {\n"
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
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(74, 74, 74);\n"
"border: 3px solid rgb(24, 103, 155);\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.btn_FAQsHash = QPushButton(self.centralwidget)
        self.btn_FAQsHash.setObjectName(u"btn_FAQsHash")
        self.btn_FAQsHash.setGeometry(QRect(342, 287, 25, 23))
        self.chkb_1 = QCheckBox(self.centralwidget)
        self.chkb_1.setObjectName(u"chkb_1")
        self.chkb_1.setGeometry(QRect(205, 6, 32, 24))
        self.chkb_1.setFont(font2)
        self.chkb_1.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.chkb_1.setChecked(False)
        self.chkb_2 = QCheckBox(self.centralwidget)
        self.chkb_2.setObjectName(u"chkb_2")
        self.chkb_2.setGeometry(QRect(246, 6, 32, 24))
        self.chkb_2.setFont(font2)
        self.chkb_2.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.chkb_2.setChecked(False)
        self.chkb_3 = QCheckBox(self.centralwidget)
        self.chkb_3.setObjectName(u"chkb_3")
        self.chkb_3.setGeometry(QRect(290, 6, 32, 24))
        self.chkb_3.setFont(font2)
        self.chkb_3.setStyleSheet(u"color: rgb(128, 200, 255);")
        self.chkb_3.setChecked(False)
        self.btn_Replace = QPushButton(self.centralwidget)
        self.btn_Replace.setObjectName(u"btn_Replace")
        self.btn_Replace.setGeometry(QRect(283, 418, 80, 80))
        self.btn_Replace.setStyleSheet(u"QPushButton {\n"
"font:10pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(34, 34, 34);\n"
"background-color: rgb(125, 125, 125);\n"
"\n"
"border: 1px solid rgb(24, 103, 155);\n"
"border-radius: 8px;\n"
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
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 380, 33))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.lbl_author.setText(QCoreApplication.translate("mainWindow", u"@HuangFei", None))
        self.lbl_Rename.setText(QCoreApplication.translate("mainWindow", u"Rename mode:", None))
        self.chkb_Hierachy.setText(QCoreApplication.translate("mainWindow", u"Hierarchy", None))
        self.chkb_Selected.setText(QCoreApplication.translate("mainWindow", u"Selected", None))
        self.chkb_All.setText(QCoreApplication.translate("mainWindow", u"All", None))
        self.btn_reNum.setText(QCoreApplication.translate("mainWindow", u"Rename and Number", None))
        self.btn_FirstChar.setText(QCoreApplication.translate("mainWindow", u"First Character -->", None))
        self.btn_LastChar.setText(QCoreApplication.translate("mainWindow", u"<-- Last Character", None))
        self.lbl_Start.setText(QCoreApplication.translate("mainWindow", u"Start:", None))
        self.lbl_Padding.setText(QCoreApplication.translate("mainWindow", u"Padding:", None))
        self.lbl_HashRename.setText(QCoreApplication.translate("mainWindow", u"Hash Rename:", None))
        self.btn_Rename.setText(QCoreApplication.translate("mainWindow", u"Rename", None))
        self.lbl_Before.setText(QCoreApplication.translate("mainWindow", u"(Before)", None))
        self.lbl_After.setText(QCoreApplication.translate("mainWindow", u"(After)", None))
        self.btn_addBefore.setText(QCoreApplication.translate("mainWindow", u"Add", None))
        self.btn_addAfter.setText(QCoreApplication.translate("mainWindow", u"Add", None))
        self.lbl_Search.setText(QCoreApplication.translate("mainWindow", u"Search:", None))
        self.lbl_Replace.setText(QCoreApplication.translate("mainWindow", u"Replace:", None))
        self.btn_Pre_01.setText(QCoreApplication.translate("mainWindow", u"Grp_", None))
        self.btn_Pre_02.setText(QCoreApplication.translate("mainWindow", u"MI_", None))
        self.btn_Pre_03.setText(QCoreApplication.translate("mainWindow", u"SM_", None))
        self.btn_Pre_04.setText(QCoreApplication.translate("mainWindow", u"SKM_", None))
        self.btn_Pre_05.setText(QCoreApplication.translate("mainWindow", u"_pkg", None))
        self.btn_Pre_06.setText(QCoreApplication.translate("mainWindow", u"More", None))
        self.lbl_Prefix.setText(QCoreApplication.translate("mainWindow", u"Prefix_ :", None))
        self.lbl_Package.setText(QCoreApplication.translate("mainWindow", u"Package:", None))
        self.btn_FAQsAll.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btn_FAQsSearch.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btn_FAQsAddPrefix.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.btn_pkgSort.setText(QCoreApplication.translate("mainWindow", u"Sort Large to Small Topo", None))
        self.btn_pkgCleanGroup.setText(QCoreApplication.translate("mainWindow", u"Clean Group", None))
        self.btn_pkgReset.setText(QCoreApplication.translate("mainWindow", u"Reset", None))
        self.btn_FAQsHash.setText(QCoreApplication.translate("mainWindow", u"?", None))
        self.chkb_1.setText(QCoreApplication.translate("mainWindow", u"1", None))
        self.chkb_2.setText(QCoreApplication.translate("mainWindow", u"2", None))
        self.chkb_3.setText(QCoreApplication.translate("mainWindow", u"3", None))
        self.btn_Replace.setText(QCoreApplication.translate("mainWindow", u"Replace", None))
    # retranslateUi

