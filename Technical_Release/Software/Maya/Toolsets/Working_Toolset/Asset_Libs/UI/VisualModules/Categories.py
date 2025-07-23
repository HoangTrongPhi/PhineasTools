"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - Hiển thị danh sách các category trong một QListView.
    - Cho phép create, delete, rename category.
    - Cập nhật danh sách category từ categories.json.
"""

import os
import json

#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets, QtCore, QtGui, QtUiTools, wrapInstance

QStyledItemDelegate = QtWidgets.QStyledItemDelegate
QPainter = QtGui.QPainter
QStyleOptionViewItem = QtWidgets.QStyleOptionViewItem
QStyle = QtWidgets.QStyle
QColor = QtGui.QColor
QSize = QtCore.QSize
Qt = QtCore.Qt
QListView = QtWidgets.QListView
QStringListModel = QtCore.QStringListModel
QPoint = QtCore.QPoint
QMenu = QtWidgets.QMenu
QMessageBox = QtWidgets.QMessageBox
Signal = QtCore.Signal
QInputDialog = QtWidgets.QInputDialog
import importlib

# -- Logic Modules
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)

CATEGORIES_JSON_PATH = config_module.Configuration.get_categories_json_path()

# ========== DELEGATE: Tùy biến giao diện item ==========
class CategoryItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.margin = 2  # spacing xung quanh mỗi item

    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index):
        text = index.data()
        painter.save()
        rect = option.rect.adjusted(self.margin, self.margin, -self.margin, -self.margin)
        if option.state & QStyle.State_Selected:
            painter.fillRect(rect, QColor("#3d6fa5"))
        elif option.state & QStyle.State_MouseOver:
            painter.fillRect(rect, QColor("#444444"))
        else:
            painter.fillRect(rect, QColor("#2e2e2e"))
        painter.setPen(QColor("#555555"))
        painter.drawRect(rect)
        painter.setPen(Qt.white)
        painter.drawText(rect.adjusted(10, 0, 0, 0), Qt.AlignVCenter | Qt.AlignLeft, text)
        painter.restore()

    def sizeHint(self, option: QStyleOptionViewItem, index):
        return QSize(option.rect.width(), 36)  # chiều cao item

# ========== DANH SÁCH CATEGORIES ==========
class Categories(QListView):

    #Signal custom
    category_selected = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)


        # Model quản lý dữ liệu category
        self.model = QStringListModel()
        self.setModel(self.model)
        self.setItemDelegate(CategoryItemDelegate(self))

        #
        self.selectionModel().selectionChanged.connect(self._on_selection_changed)

        # edit triggers để cho phép đổi tên category bằng double click
        self.setEditTriggers(QListView.DoubleClicked | QListView.SelectedClicked)
        # listen thay đổi tên
        self.model.dataChanged.connect(self.on_category_renamed)

        # Thiết lập context menu chuột phải
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.open_context_menu)
        self.setFixedHeight(150)
        self.setFixedWidth(201)


        self.load_categories()

        # click chọn category sẽ phát tín hiệu
        self.clicked.connect(self.on_item_clicked)

    def on_item_clicked(self, index):
        category = self.model.data(index, Qt.DisplayRole)
        self.category_selected.emit(category)  # Emit signal khi click


    def open_context_menu(self, pos: QPoint):
        """Tạo menu chuột phải để thêm, xóa, đổi tên category"""
        menu = QMenu(self)
        add_action = menu.addAction("Add Category")
        rename_action = menu.addAction("Rename Category")
        del_action = menu.addAction("Delete Category")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == add_action:
            self.add_category()
        elif action == del_action:
            self.delete_category()
        elif action == rename_action:
            self.rename_category()

    def add_category(self):
        text, ok = QInputDialog.getText(self, "Add Category", "Category name:")
        if ok and text:
            categories = self.model.stringList()
            if text not in categories:
                categories.append(text)
                self.model.setStringList(categories)
                self.save_categories()
                self._old_categories = list(categories)
            else:
                QMessageBox.warning(self, "Duplicate", "Category đã tồn tại.")


    def delete_category(self):
        index = self.currentIndex()
        if index.isValid():
            categories = self.model.stringList()
            del categories[index.row()]
            self.model.setStringList(categories)
            self.save_categories()
            self._old_categories = list(categories)

    def rename_category(self):
        index = self.currentIndex()
        if not index.isValid():
            QMessageBox.warning(self, "Rename Category", "Chọn Category để rename.")
            return
        old_name = self.model.data(index, Qt.DisplayRole)
        text, ok = QInputDialog.getText(self, "Rename Category", "New category name:", text=old_name)
        if ok and text:
            categories = self.model.stringList()
            if text in categories:
                QMessageBox.warning(self, "Duplicate", "Category đã tồn tại.")
                return
            categories[index.row()] = text
            self.model.setStringList(categories)
            self.save_categories()
            self._old_categories = list(categories)

    def on_category_renamed(self, topLeft, bottomRight, roles):
        """
        Khi người dùng sửa tên category trực tiếp:
        - Nếu tên mới trùng tên khác, phục hồi tên cũ và cảnh báo.
        - Ngược lại, lưu vào file json.
        """
        new_categories = self.model.stringList()
        # Kiểm tra trùng tên (số lượng phần tử phải = số lượng set)
        if len(new_categories) != len(set(new_categories)):
            # Nếu trùng, revert lại model cũ và báo lỗi
            QMessageBox.warning(self, "Duplicate", "Category đã tồn tại.")
            self.model.setStringList(self._old_categories)
        else:
            # Nếu không trùng, lưu và cập nhật danh sách tạm
            self.save_categories()
            self._old_categories = list(new_categories)

    def _on_selection_changed(self, selected, deselected):
        if not selected.indexes():
            return
        index = selected.indexes()[0]
        category_name = index.data()
        self.category_selected.emit(category_name)

    def save_categories(self):
        """Ghi danh sách category vào JSON"""
        data = {
            "categories": self.model.stringList()
        }
        try:
            with open(CATEGORIES_JSON_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except:
            existing = {}
        existing["categories"] = data["categories"]
        with open(CATEGORIES_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(existing, f, indent=4, ensure_ascii=False)

    def load_categories(self):
        """Đọc danh sách category từ JSON"""
        if not os.path.exists(CATEGORIES_JSON_PATH):
            return
        with open(CATEGORIES_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.model.setStringList(data.get("categories", []))
        self._old_categories = self.model.stringList()


# ========== HÀM LÀM MỚI DANH SÁCH CATEGORIES ==========
    def refresh_categories(comboBox):
        """
        Làm mới danh sách category cho comboBox filter (cbb_tableView) ở MainWindow.
        """
        comboBox.blockSignals(True)
        comboBox.clear()
        comboBox.addItem("All")
        category_path = config_module.Configuration.get_categories_json_path()
        if os.path.exists(category_path):
            with open(category_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                categories = data.get("categories", [])
                comboBox.addItems(sorted(categories))
        comboBox.blockSignals(False)
