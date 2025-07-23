"""
    Author: Hoàng Trọng Phi
    25/6/2025
    Chức năng:
    - Hiển thị danh sách asset trong một thư mục lên QTableWidget
    - Hỗ trợ phân loại asset theo category
    - Tự động tạo thumbnail từ file asset nếu có
    - Hỗ trợ cập nhật assignments.json để phân loại asset, tên <asset_name> : <category>
"""

import os
import json

class AssetTable:
    def __init__(self, table_widget, asset_folder, assignments_dict, max_columns=4, item_widget_cls=None):
        """
        table_widget: QTableWidget instance
        asset_folder: path tới folder chứa asset
        assignments_dict: dict {basename: category} hoặc path string (tự động convert)
        max_columns: số cột mỗi dòng
        item_widget_cls: class widget đại diện cho mỗi asset (mặc định None, sẽ tạo QLabel)
        """
        self.table_widget = table_widget
        self.asset_folder = asset_folder
        self.assignments_dict = self._ensure_dict(assignments_dict)
        self.max_columns = max_columns
        self.item_widget_cls = item_widget_cls

    def _ensure_dict(self, data):
        """
        Đảm bảo dữ liệu là dict. Nếu là string, tự đọc file json.
        """
        if isinstance(data, dict):
            return data
        if isinstance(data, str) and os.path.exists(data):
            try:
                with open(data, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print("Lỗi đọc assignments_dict:", e)
        # fallback
        return {}

    def populate(self, category="all"):
        """
        Hiển thị các asset theo category lên tableWidget.
        """
        # 1. Lấy danh sách file asset
        all_files = []
        for root, dirs, files in os.walk(self.asset_folder):
            for f in files:
                if f.lower().endswith(('.fbx', '.obj')):
                    all_files.append(os.path.join(root, f))

        # 2. Lọc theo category
        filtered_files = []
        for path in all_files:
            base = os.path.splitext(os.path.basename(path))[0]
            if not self.assignments_dict:  # Nếu không có assignment nào, luôn cho hiện tất cả file
                filtered_files.append(path)
            else:
                assigned = self.assignments_dict.get(base, "").lower()
                if category.lower() == "all" or assigned == category.lower():
                    filtered_files.append(path)

        total_items = len(filtered_files)
        rows = (total_items + self.max_columns - 1) // self.max_columns

        # 3. Reset table
        self.table_widget.clearContents()
        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(self.max_columns)

        for col in range(self.max_columns):
            self.table_widget.setColumnWidth(col, 192)
        for row in range(rows):
            self.table_widget.setRowHeight(row, 192)

        # 4. Reset toàn bộ cell về QWidget rỗng
        for i in range(rows * self.max_columns):
            r = i // self.max_columns
            c = i % self.max_columns
            self.table_widget.setCellWidget(r, c, None)

        # 5. Thêm widget cho từng asset
        for index, file_path in enumerate(filtered_files):
            row = index // self.max_columns
            col = index % self.max_columns
            if self.item_widget_cls is not None:
                item_widget = self.item_widget_cls(file_path)
            else:
                from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
                from PySide6.QtGui import QPixmap
                from PySide6.QtCore import Qt
                item_widget = QWidget()
                layout = QVBoxLayout(item_widget)
                base = os.path.splitext(os.path.basename(file_path))[0]
                lbl = QLabel(base)
                layout.addWidget(lbl)
                thumbnail_path = os.path.splitext(file_path)[0] + ".png"
                img_label = QLabel()
                if os.path.exists(thumbnail_path):
                    pixmap = QPixmap(thumbnail_path)
                    img_label.setPixmap(pixmap.scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                layout.addWidget(img_label)
                item_widget.setLayout(layout)
                item_widget.setFixedSize(192, 192)

            self.table_widget.setCellWidget(row, col, item_widget)

    def update_assignments(self, new_assignments_dict):
        """
        Cập nhật assignments_dict, luôn tự kiểm tra kiểu dữ liệu.
        """
        self.assignments_dict = self._ensure_dict(new_assignments_dict)

    def update_folder(self, new_asset_folder):
        self.asset_folder = new_asset_folder

    def refresh(self, category="all"):
        self.populate(category)

    def populate_with_filelist(self, filelist):
        self.table_widget.clearContents()
        max_columns = self.max_columns
        total_items = len(filelist)
        rows = (total_items + max_columns - 1) // max_columns
        self.table_widget.setRowCount(rows)
        self.table_widget.setColumnCount(max_columns)
        for col in range(max_columns):
            self.table_widget.setColumnWidth(col, 192)
        for row in range(rows):
            self.table_widget.setRowHeight(row, 192)

        for idx, file_path in enumerate(filelist):
            row = idx // max_columns
            col = idx % max_columns
            if self.item_widget_cls is not None:
                item_widget = self.item_widget_cls(file_path)
            else:
                # Nếu không truyền class widget riêng thì tạo label mặc định
                from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
                from PySide6.QtGui import QPixmap
                from PySide6.QtCore import Qt
                item_widget = QWidget()
                layout = QVBoxLayout(item_widget)
                base = os.path.splitext(os.path.basename(file_path))[0]
                lbl = QLabel(base)
                layout.addWidget(lbl)
                thumbnail_path = os.path.splitext(file_path)[0] + ".png"
                img_label = QLabel()
                if os.path.exists(thumbnail_path):
                    pixmap = QPixmap(thumbnail_path)
                    img_label.setPixmap(pixmap.scaled(160, 160, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                layout.addWidget(img_label)
                item_widget.setLayout(layout)
                item_widget.setFixedSize(192, 192)

            self.table_widget.setCellWidget(row, col, item_widget)
        # Đảm bảo UI được update
        self.table_widget.repaint()

