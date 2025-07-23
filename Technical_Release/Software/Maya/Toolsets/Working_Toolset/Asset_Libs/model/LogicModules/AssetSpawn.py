"""
    Author: Hoàng Trọng Phi
    26/6/2025
    Chức năng:
    - Nhập các file FBX/OBJ vào Maya.
    - Tự động gán shading group cho mesh mới nhập.
    - Đổi tên transform node cha của mesh thành đúng tên namespace.
    - Đọc thông tin metadata từ mesh_data.json để xác định key namespace.
    - Trả về danh sách các mesh đã nhập.

"""
import os
import json
import maya.cmds as cmds

import importlib
import Software.Maya.Toolsets.Working_Toolset.Asset_Libs.model.LogicModules.Configuration as Config
importlib.reload(Config)

# Đường dẫn file mesh_data.json (chuẩn lấy từ config)
MESH_DATA_PATH = Config.Configuration.get_mesh_data_json_path()

class AssetSpawner:
    """
    Chức năng chính:
        - spawn_asset(file_path): Nhập file FBX/OBJ vào Maya, trả về danh sách các mesh đã nhập.
        - Đọc thông tin metadata từ mesh_data.json để xác định key namespace.
        - Tự động gán shading group cho mesh mới nhập.
        - Đổi tên transform node cha của mesh thành đúng tên namespace.
    """
    @staticmethod
    def spawn_asset(file_path):  # <-- truyền vào là path đến FBX/OBJ
        if not os.path.exists(file_path):
            cmds.warning(f"Asset not found: {file_path}")
            return []

        ext = os.path.splitext(file_path)[1].lower()  # Lấy loại file (.fbx, .obj...)
        base_name = os.path.splitext(os.path.basename(file_path))[0]  # Lấy tên mesh (không extension)

        # Đọc mesh_data.json để xác định key namespace
        try:
            with open(MESH_DATA_PATH, 'r', encoding='utf-8') as f:
                mesh_data = json.load(f)
            # Nếu không tồn tại key thì báo lỗi
            mesh_key = f"{base_name}{ext}"
            if mesh_key not in mesh_data:
                cmds.warning(f"Mesh name {base_name} not found in mesh_data.json.")
                return []
        except Exception as e:
            cmds.warning(f"Error reading mesh_data.json: {str(e)}")
            return []

        namespace = base_name  # namespace là tên mesh (không chứa .fbx/.obj)

        IMPORT_OPTIONS = {
            '.fbx': {'type': 'FBX', 'options': 'fbx'},
            '.obj': {'type': 'OBJ', 'options': 'obj'},
            # Có thể mở rộng định dạng mới ở đây
        }

        if ext not in IMPORT_OPTIONS:
            cmds.warning("Unsupported file format: " + ext)
            return []

        try:
            import_opt = IMPORT_OPTIONS[ext]
            imported_nodes = cmds.file(
                file_path,
                i=True,
                type=import_opt['type'],
                ignoreVersion=True,
                ra=True,
                mergeNamespacesOnClash=False,
                namespace=namespace,
                options=import_opt['options'],
                pr=True,
                returnNewNodes=True
            )

            # Lấy các transform node chứa mesh vừa import
            imported_meshes = cmds.ls(imported_nodes, type="mesh", long=True)
            for mesh in imported_meshes:
                shading_groups = cmds.listConnections(mesh, type='shadingEngine') or []
                if 'initialShadingGroup' not in shading_groups:
                    for sg in shading_groups:
                        cmds.sets(mesh, e=True, remove=sg)
                    cmds.sets(mesh, e=True, forceElement='initialShadingGroup')

            # Đổi tên transform node cha của mesh thành đúng tên namespace
            if imported_meshes:
                # Lấy transform cha (transform node) của mesh đầu tiên
                mesh_transform = cmds.listRelatives(imported_meshes[0], parent=True, fullPath=True)[0]
                new_name = f"{namespace}"
                # Kiểm tra nếu đã tồn tại tên này thì đặt thêm hậu tố
                if cmds.objExists(new_name):
                    new_name = cmds.rename(mesh_transform, f"{namespace}_ver")
                else:
                    new_name = cmds.rename(mesh_transform, new_name)
                # Có thể trả về tên mới để biết chắc
                return [new_name]
            return imported_meshes


        except Exception as e:
            cmds.warning(f"Failed to import {file_path}: {str(e)}")
            return []
