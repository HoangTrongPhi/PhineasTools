# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AssetLibs_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance
from Software.Maya.Toolsets.Working_Toolset.Rename.UI.Rename import QCheckBox

QWidget = QtWidgets.QWidget
QFrame = QtWidgets.QFrame
QSizePolicy = QtWidgets.QSizePolicy
QVBoxLayout = QtWidgets.QVBoxLayout
QLabel = QtWidgets.QLabel
QPushButton = QtWidgets.QPushButton
QRect = QtCore.QRect
QCoreApplication = QtCore.QCoreApplication
QMetaObject = QtCore.QMetaObject
Qt = QtCore.Qt
QLayout = QtWidgets.QLayout
QAction = QtWidgets.QAction
QComboBox = QtWidgets.QComboBox
QListView = QtWidgets.QListView
QTreeView = QtWidgets.QTreeView
QTableWidget = QtWidgets.QTableWidget
QRadioButton = QtWidgets.QRadioButton
QMenuBar = QtWidgets.QMenuBar
QMenu = QtWidgets.QMenu
QCheckBox = QtWidgets.QCheckBox
QStatusBar = QtWidgets.QStatusBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(920, 632)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.actionSet_Library_Path = QAction(MainWindow)
        self.actionSet_Library_Path.setObjectName(u"actionSet_Library_Path")
        self.actionRefresh = QAction(MainWindow)
        self.actionRefresh.setObjectName(u"actionRefresh")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpenExplore = QAction(MainWindow)
        self.actionOpenExplore.setObjectName(u"actionOpenExplore")
        self.actionSort_All_With_FBX = QAction(MainWindow)
        self.actionSort_All_With_FBX.setObjectName(u"actionSort_All_With_FBX")
        self.actionSort_All_with_OBJ = QAction(MainWindow)
        self.actionSort_All_with_OBJ.setObjectName(u"actionSort_All_with_OBJ")
        self.actionSort_All_with_USD = QAction(MainWindow)
        self.actionSort_All_with_USD.setObjectName(u"actionSort_All_with_USD")
        self.actionSort_with_Texture = QAction(MainWindow)
        self.actionSort_with_Texture.setObjectName(u"actionSort_with_Texture")
        self.actionComming_Soon = QAction(MainWindow)
        self.actionComming_Soon.setObjectName(u"actionComming_Soon")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.actionDocumentation_2 = QAction(MainWindow)
        self.actionDocumentation_2.setObjectName(u"actionDocumentation_2")
        self.actionCall_Phineas = QAction(MainWindow)
        self.actionCall_Phineas.setObjectName(u"actionCall_Phineas")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView_Categories = QListView(self.centralwidget)
        self.listView_Categories.setObjectName(u"listView_Categories")
        self.listView_Categories.setGeometry(QRect(10, 390, 200, 150))
        self.listView_Categories.setStyleSheet(u"QListView {\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.treeView_libs = QTreeView(self.centralwidget)
        self.treeView_libs.setObjectName(u"treeView_libs")
        self.treeView_libs.setGeometry(QRect(10, 41, 200, 330))
        self.treeView_libs.setStyleSheet(u"QTreeView {\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.lbl_Library = QLabel(self.centralwidget)
        self.lbl_Library.setObjectName(u"lbl_Library")
        self.lbl_Library.setGeometry(QRect(14, 14, 50, 16))
        self.lbl_Library.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Categories = QLabel(self.centralwidget)
        self.lbl_Categories.setObjectName(u"lbl_Categories")
        self.lbl_Categories.setGeometry(QRect(14, 372, 161, 16))
        self.lbl_Categories.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(220, 40, 690, 500))
        self.tableWidget.setStyleSheet(u"QTableWidget::item {\n"
"    border: 1px solid gray;\n"
"    margin: 1px;  /* t\u1ea1o c\u1ea3m gi\u00e1c kho\u1ea3ng tr\u1ed1ng */\n"
"    padding: 1px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: transparent;  /* \u1ea9n grid g\u1ed1c n\u1ebfu mu\u1ed1n */\n"
"	border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(192)
        self.tableWidget.verticalHeader().setMinimumSectionSize(192)
        self.cbb_tableView = QComboBox(self.centralwidget)
        self.cbb_tableView.setObjectName(u"cbb_tableView")
        self.cbb_tableView.setGeometry(QRect(577, 2, 291, 32))
        self.cbb_tableView.setStyleSheet(u"QComboBox {\n"
"	color: rgb(128, 200, 255);\n"
"	background-color: rgb(36, 36, 36); \n"
"	border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.btn_Add = QPushButton(self.centralwidget)
        self.btn_Add.setObjectName(u"btn_Add")
        self.btn_Add.setGeometry(QRect(220, 543, 160, 35))
        self.btn_Add.setStyleSheet(u"QPushButton {\n"
"    font: 10pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: rgb(230, 230, 230);                        \n"
"    background-color: rgb(60, 60, 60);                \n"
"    \n"
"    border: 1px solid rgb(61, 111, 165);              \n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(80, 80, 80);               \n"
"    border: 2px solid rgb(61, 111, 165);               \n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(46, 46, 46);                 \n"
"    border: 2px solid rgb(61, 111, 165);\n"
"    border-radius: 8px;\n"
"}\n"
"")
        self.btn_FAQs = QPushButton(self.centralwidget)
        self.btn_FAQs.setObjectName(u"btn_FAQs")
        self.btn_FAQs.setGeometry(QRect(875, 2, 32, 32))
        self.lbl_author = QLabel(self.centralwidget)
        self.lbl_author.setObjectName(u"lbl_author")
        self.lbl_author.setGeometry(QRect(10, 550, 72, 20))
        self.lbl_author.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_FAQs = QLabel(self.centralwidget)
        self.lbl_FAQs.setObjectName(u"lbl_FAQs")
        self.lbl_FAQs.setGeometry(QRect(399, 553, 512, 20))
        self.lbl_FAQs.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.rbtn_FBX = QRadioButton(self.centralwidget)
        self.rbtn_FBX.setObjectName(u"rbtn_FBX")
        self.rbtn_FBX.setEnabled(True)
        self.rbtn_FBX.setGeometry(QRect(387, 14, 50, 20))
        self.rbtn_FBX.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.rbtn_OBJ = QRadioButton(self.centralwidget)
        self.rbtn_OBJ.setObjectName(u"rbtn_OBJ")
        self.rbtn_OBJ.setGeometry(QRect(440, 14, 50, 20))
        self.rbtn_OBJ.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.rbtn_USD = QRadioButton(self.centralwidget)
        self.rbtn_USD.setObjectName(u"rbtn_USD")
        self.rbtn_USD.setGeometry(QRect(491, 14, 61, 20))
        self.rbtn_USD.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.rbtn_All = QRadioButton(self.centralwidget)
        self.rbtn_All.setObjectName(u"rbtn_All")
        self.rbtn_All.setEnabled(True)
        self.rbtn_All.setGeometry(QRect(336, 14, 50, 20))
        self.rbtn_All.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.lbl_Filter_type = QLabel(self.centralwidget)
        self.lbl_Filter_type.setObjectName(u"lbl_Filter_type")
        self.lbl_Filter_type.setGeometry(QRect(272, 13, 62, 20))
        self.lbl_Filter_type.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        self.ckb_treeFolder = QCheckBox(self.centralwidget)
        self.ckb_treeFolder.setObjectName(u"ckb_treeFolder")
        self.ckb_treeFolder.setGeometry(QRect(68, 13, 112, 20))
        self.ckb_treeFolder.setStyleSheet(u"color: rgb(128, 200, 255);\n"
"font:10pt  \"Bahnschrift SemiBold SemiConden\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 920, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSet_Library_Path)
        self.menuFile.addAction(self.actionRefresh)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpenExplore)
        self.menuFile.addAction(self.actionComming_Soon)
        self.menuView.addAction(self.actionSort_All_With_FBX)
        self.menuView.addAction(self.actionSort_All_with_OBJ)
        self.menuView.addAction(self.actionSort_All_with_USD)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionSort_with_Texture)
        self.menuHelp.addAction(self.actionDocumentation_2)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCall_Phineas)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSet_Library_Path.setText(QCoreApplication.translate("MainWindow", u"Set Library Path", None))
        self.actionRefresh.setText(QCoreApplication.translate("MainWindow", u"Refresh Library", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionOpenExplore.setText(QCoreApplication.translate("MainWindow", u"Open Explore", None))
        self.actionSort_All_With_FBX.setText(QCoreApplication.translate("MainWindow", u"Sort All with FBX", None))
        self.actionSort_All_with_OBJ.setText(QCoreApplication.translate("MainWindow", u"Sort  All with OBJ", None))
        self.actionSort_All_with_USD.setText(QCoreApplication.translate("MainWindow", u"Sort All with USD", None))
        self.actionSort_with_Texture.setText(QCoreApplication.translate("MainWindow", u"CommingSoon", None))
        self.actionComming_Soon.setText(QCoreApplication.translate("MainWindow", u"Comming Soon", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"Call Phineas ", None))
        self.actionDocumentation_2.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.actionCall_Phineas.setText(QCoreApplication.translate("MainWindow", u"Call Phineas", None))
        self.lbl_Library.setText(QCoreApplication.translate("MainWindow", u"Library:", None))
        self.lbl_Categories.setText(QCoreApplication.translate("MainWindow", u"Categories:", None))
        self.btn_Add.setText(QCoreApplication.translate("MainWindow", u"Add Object", None))
        self.btn_FAQs.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.lbl_author.setText(QCoreApplication.translate("MainWindow", u"@HuangFei", None))
        self.lbl_FAQs.setText(QCoreApplication.translate("MainWindow", u"tip: C\u00f3 th\u1ec3 t\u1ea1o folder theo ng\u00e0y, version, qu\u1ea3n l\u00fd categories theo t\u1eebng ph\u1ea7n c\u1ee7a project", None))
        self.rbtn_FBX.setText(QCoreApplication.translate("MainWindow", u"FBX", None))
        self.rbtn_OBJ.setText(QCoreApplication.translate("MainWindow", u"OBJ", None))
        self.rbtn_USD.setText(QCoreApplication.translate("MainWindow", u"USDZ", None))
        self.rbtn_All.setText(QCoreApplication.translate("MainWindow", u"ALL", None))
        self.lbl_Filter_type.setText(QCoreApplication.translate("MainWindow", u"Filter type:", None))
        self.ckb_treeFolder.setText(QCoreApplication.translate("MainWindow", u"Sort wtih folder", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

