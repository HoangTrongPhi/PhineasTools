# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelkit.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ModelKitDialog(object):
    def setupUi(self, ModelKitDialog):
        if not ModelKitDialog.objectName():
            ModelKitDialog.setObjectName(u"ModelKitDialog")
        ModelKitDialog.resize(625, 220)
        ModelKitDialog.setMinimumSize(QSize(625, 220))
        self.main_layout = QVBoxLayout(ModelKitDialog)
        self.main_layout.setSpacing(2)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.verticalSpacer = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_layout.addItem(self.verticalSpacer)

        self.lib_loader_layout = QHBoxLayout()
        self.lib_loader_layout.setObjectName(u"lib_loader_layout")
        self.libraryload_lable = QLabel(ModelKitDialog)
        self.libraryload_lable.setObjectName(u"libraryload_lable")

        self.lib_loader_layout.addWidget(self.libraryload_lable)

        self.libraryload_le = QLineEdit(ModelKitDialog)
        self.libraryload_le.setObjectName(u"libraryload_le")

        self.lib_loader_layout.addWidget(self.libraryload_le)

        self.select_lib_path_btn = QPushButton(ModelKitDialog)
        self.select_lib_path_btn.setObjectName(u"select_lib_path_btn")
        icon = QIcon()
        icon.addFile(u":fileOpen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.select_lib_path_btn.setIcon(icon)

        self.lib_loader_layout.addWidget(self.select_lib_path_btn)

        self.load_library_btn = QPushButton(ModelKitDialog)
        self.load_library_btn.setObjectName(u"load_library_btn")

        self.lib_loader_layout.addWidget(self.load_library_btn)


        self.main_layout.addLayout(self.lib_loader_layout)

        self.table_wdg = QTableWidget(ModelKitDialog)
        if (self.table_wdg.columnCount() < 5):
            self.table_wdg.setColumnCount(5)
        if (self.table_wdg.rowCount() < 1):
            self.table_wdg.setRowCount(1)
        self.table_wdg.setObjectName(u"table_wdg")
        self.table_wdg.setRowCount(1)
        self.table_wdg.setColumnCount(5)

        self.main_layout.addWidget(self.table_wdg)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.horizontalSpacer = QSpacerItem(2, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.horizontalSpacer_2)

        self.add_btn = QPushButton(ModelKitDialog)
        self.add_btn.setObjectName(u"add_btn")

        self.button_layout.addWidget(self.add_btn)

        self.close_btn = QPushButton(ModelKitDialog)
        self.close_btn.setObjectName(u"close_btn")

        self.button_layout.addWidget(self.close_btn)


        self.main_layout.addLayout(self.button_layout)


        self.retranslateUi(ModelKitDialog)

        QMetaObject.connectSlotsByName(ModelKitDialog)
    # setupUi

    def retranslateUi(self, ModelKitDialog):
        ModelKitDialog.setWindowTitle(QCoreApplication.translate("ModelKitDialog", u"Phineas Model Kit", None))
        self.libraryload_lable.setText(QCoreApplication.translate("ModelKitDialog", u"Library Folder", None))
        self.select_lib_path_btn.setText("")
        self.load_library_btn.setText(QCoreApplication.translate("ModelKitDialog", u"Load Existing", None))
        self.add_btn.setText(QCoreApplication.translate("ModelKitDialog", u"Add Object", None))
        self.close_btn.setText(QCoreApplication.translate("ModelKitDialog", u"Close", None))
    # retranslateUi

