"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - Export Mesh theo định dạng  .fbx, .obj, .usd ( sẽ cập nhật sau)
    - Tạo Thumbnail cho Asset
    - Lưu metadata (triangle count) cho asset export vào mesh_data.json (trong thư mục chứa config.json, cạnh Configuration.py)
"""

import maya.cmds as cmds
import os
#------- PyQt/PySide imports ----------
from Common.qt_compat import QtWidgets


import importlib
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as config_module
importlib.reload(config_module)

class AssetExport:
    """
        Layout AssetExport
        Chức năng:
        - Export Mesh theo định dạng  .fbx, .obj, .usd ( sẽ cập nhật sau)
        - Tạo Thumbnail cho Asset
        - Lưu metadata (triangle count) cho asset export vào mesh_data.json (trong thư mục chứa config.json, cạnh Configuration.py)
    """

    @staticmethod
    def export_selected_mesh(parent, export_dir):
        # Lấy các mesh đang được chọn trong Maya
        selection = cmds.ls(selection=True, dag=True, type='mesh')
        if not selection:
            # Nếu không có mesh nào được chọn thì cảnh báo và thoát
            QtWidgets.QMessageBox.warning(parent, "No Mesh", "Please select a mesh in Maya.")
            return None, None

        # Lấy node cha (transform node) của mesh đầu tiên
        mesh_transform = cmds.listRelatives(selection[0], parent=True, fullPath=True)[0]

        dialog = QtWidgets.QDialog(parent)
        dialog.setWindowTitle("Export Selected Mesh")
        layout = QtWidgets.QFormLayout(dialog)

        name_input = QtWidgets.QLineEdit(dialog)  # Nhập tên file
        format_combo = QtWidgets.QComboBox(dialog)  # Combo box chọn định dạng file
        format_combo.addItems([".fbx", ".obj"])  # Thêm hai định dạng xuất ra

        layout.addRow("File Name:", name_input)
        layout.addRow("Format:", format_combo)

        # Tạo nút OK và Cancel
        buttons = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addWidget(buttons)

        if dialog.exec_():
            name = name_input.text().strip()  # Lấy tên file từ input
            ext = format_combo.currentText()  # Lấy phần mở rộng file từ combo box

            # Tạo thư mục nếu chưa tồn tại
            if not os.path.isdir(export_dir):
                os.makedirs(export_dir)

            # Tạo đường dẫn đầy đủ tới file export
            export_path = os.path.join(export_dir, f"{name}{ext}")

            # Chọn object để export
            cmds.select(mesh_transform, r=True)

            # Export theo định dạng
            if ext == ".fbx":
                cmds.file(export_path, force=True, options="v=0;", type="FBX export", pr=True, es=True)
            else:
                cmds.file(export_path, force=True, options="groups=1;ptgroups=1;materials=1;smoothing=1;normals=1", type="OBJexport", pr=True, es=True)

            thumbnail_path = os.path.join(export_dir, f"{name}.png")
            AssetExport.generate_thumbnail(mesh_transform, thumbnail_path)

            # >>>> Lưu metadata (triangle count) vào mesh_data.json DUY NHẤT (cạnh config.json) <<<<
            AssetExport.save_mesh_data(export_path, mesh_transform)

            return export_path, thumbnail_path
        return None, None

    @staticmethod
    def generate_thumbnail(object_name, save_path):
        camera_distance_offset = 1.0  # <-- Đặt biến offset tại đây (đơn vị Maya)

        # Tạo camera mới để chụp ảnh thumbnail
        camera = cmds.camera(name="ThumbnailCam")[0]
        cmds.select(object_name, r=True)
        cmds.lookThru(camera)
        cmds.viewFit(camera, all=False)  # Zoom vừa khung hình

        # Lùi camera ra xa hơn (sau khi đã viewFit)
        if camera_distance_offset != 0.0:
            cam_matrix = cmds.xform(camera, query=True, matrix=True, worldSpace=True)
            z_vec = [cam_matrix[8], cam_matrix[9], cam_matrix[10]]
            cam_pos = cmds.xform(camera, query=True, translation=True, worldSpace=True)
            new_pos = [
                cam_pos[0] + z_vec[0] * camera_distance_offset,
                cam_pos[1] + z_vec[1] * camera_distance_offset,
                cam_pos[2] + z_vec[2] * camera_distance_offset
            ]
            cmds.xform(camera, translation=new_pos, worldSpace=True)

        cmds.playblast(
            completeFilename=save_path,
            format='image',
            frame=cmds.currentTime(query=True),
            width=128,
            height=128,
            showOrnaments=False,
            viewer=False,
            percent=150,
            offScreen=True
        )
        cmds.delete(camera)

    @staticmethod
    def save_mesh_data(export_path, mesh_transform):
        """
        Lưu thông tin metadata (triangle count) của asset export vào mesh_data.json duy nhất
        """
        meshes = cmds.listRelatives(mesh_transform, allDescendents=True, type='mesh', fullPath=True) or []
        if not meshes and cmds.objectType(mesh_transform) == 'mesh':
            meshes = [mesh_transform]
        triangle_count = sum(cmds.polyEvaluate(m, triangle=True) for m in meshes)

        #truyền 3 tham số
        config_module.Configuration.set_mesh_data(
            os.path.basename(export_path),  # chỉ tên file, không full path
            triangle_count,
            export_path  # lưu đúng path asset
        )
