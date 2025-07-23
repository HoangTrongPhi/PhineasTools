"""
    Author: Hoàng Trọng Phi
    23/6/2025
    Chức năng:
    - Quản lý cấu hình cho Asset Library
    - Lưu trữ thông tin về đường dẫn thư viện, phân loại, metadata của mesh, v.v.
    - Cung cấp các phương thức để load/save cấu hình từ/đến file JSON.
    - Cung cấp các phương thức để quản lý phân loại, metadata của mesh, v.v.
"""
import os
import json

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

class Configuration:
    """
        Chức năng chính:
        - Save/ Load .json
        - config.json save 'asset_library_path'
        - assginment.json  save     {<asset_name>: <'name_Categories_1'>}
        - categories.json  save { categories: ['name_Categories_1', 'name_Categories_2'] }
        - mesh_data.json   save { <asset_filename>: { 'triangle_count': <int>, 'file_path': <str> } }
        -
    """
    #----  Load / Save '.json'
    @staticmethod
    def load():
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r", encoding="utf-8") as f:  # Thêm encoding ở đây
                return json.load(f)
        return {}

    @staticmethod
    def save(data):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    #--------- Asset Library Path -----------
    @staticmethod
    def get_asset_library_path():
        return Configuration.load().get("asset_library_path", "")

    @staticmethod
    def set_asset_library_path(path):
        config = Configuration.load()
        config["asset_library_path"] = path
        Configuration.save(config)

    @staticmethod
    def get_categories_json_path():
        return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "categories.json"))


    # --------- Mesh Metadata (Triangle, v.v...) ----------
    @staticmethod
    def get_mesh_data_json_path():
        """
        Trả về đường dẫn tuyệt đối tới mesh_data.json (lưu toàn bộ thông tin metadata asset).
        """
        return os.path.normpath(os.path.join(os.path.dirname(__file__), "mesh_data.json"))

    @staticmethod
    def get_mesh_data(asset_filename):
        """
        Đọc thông tin data (vd: triangle count) của mesh asset từ mesh_data.json
        asset_filename: chỉ là tên file, ví dụ 'tenAsset.fbx'
        Trả về dict nếu tìm thấy, nếu không trả về {}
        """
        try:
            meta_path = Configuration.get_mesh_data_json_path()
            if not os.path.exists(meta_path):
                return {}
            with open(meta_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
            return metadata.get(asset_filename, {})
        except Exception:
            return {}

    @staticmethod
    def set_mesh_data(asset_filename, triangle_count, file_path):
        """
        Ghi hoặc cập nhật data cho mesh asset vào mesh_data.json
        asset_filename: chỉ là tên file, ví dụ 'tenAsset.fbx'
        triangle_count: số lượng triangle (int)
        file_path: string (đường dẫn tới asset)
        """
        try:
            meta_path = Configuration.get_mesh_data_json_path()
            if os.path.exists(meta_path):
                with open(meta_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            else:
                metadata = {}
            metadata[asset_filename] = {
                "triangle_count": triangle_count,
                "file_path": file_path
            }
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
            return True
        except Exception:
            return False

    @staticmethod
    def clean_mesh_data():
        """
        Xóa những key trong mesh_data.json nếu file asset tương ứng không còn tồn tại trên ổ cứng.
        Đường dẫn asset lấy từ 'file_path' bên trong value.
        """
        meta_path = Configuration.get_mesh_data_json_path()
        if not os.path.exists(meta_path):
            return
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
            # Lọc lại: chỉ giữ những asset thật sự còn tồn tại
            cleaned = {}
            for asset_name, data in metadata.items():
                asset_file = data.get("file_path", "")
                if asset_file and os.path.isfile(asset_file):
                    cleaned[asset_name] = data
            # Ghi lại nếu khác
            if cleaned != metadata:
                with open(meta_path, "w", encoding="utf-8") as f:
                    json.dump(cleaned, f, indent=4)
        except Exception:
            pass  # hoặc log nếu cần

    @staticmethod
    def remove_mesh_data(asset_filename):
        """
        Xóa metadata của asset_filename (tên file, vd: 'tenAsset.fbx') khỏi mesh_data.json.
        """
        meta_path = Configuration.get_mesh_data_json_path()
        if not os.path.exists(meta_path):
            return
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
            if asset_filename in metadata:
                del metadata[asset_filename]
                with open(meta_path, "w", encoding="utf-8") as f:
                    json.dump(metadata, f, indent=4)
        except Exception:
            pass

    @staticmethod
    def rename_mesh_data(old_filename, new_filename):
        mesh_data_path = Configuration.get_mesh_data_json_path()
        if not os.path.exists(mesh_data_path):
            return
        with open(mesh_data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if old_filename not in data:
            return
        data[new_filename] = data.pop(old_filename)
        with open(mesh_data_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    # --------- Assignments -----------
    @staticmethod
    def get_assignments_json_path():
        return os.path.normpath(os.path.join(os.path.dirname(__file__), "assignments.json"))

    @staticmethod
    def get_assignments_dict():
        path = Configuration.get_assignments_json_path()
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    @staticmethod
    def load_assignments():
        path = Configuration.get_assignments_json_path()
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:  # Thêm encoding ở đây
                return json.load(f)
        return {}

    @staticmethod
    def save_assignments(data):
        path = Configuration.get_assignments_json_path()
        with open(path, "w", encoding="utf-8") as f:  # Thêm encoding ở đây
            json.dump(data, f, indent=4)


    @staticmethod
    def cleaned_assignments(default_category="All"):
        """
        - Nếu key trong assignments.json không còn file thật sự, xóa key đó.
        - Nếu có asset mới (file .fbx/.obj) chưa có key, thêm key với value = default_category.
        - Ghi assignments.json luôn phản ánh đúng asset_folder hiện tại.
        """
        asset_folder = Configuration.get_asset_library_path()
        assignments_path = Configuration.get_assignments_json_path()
        if not os.path.exists(asset_folder):
            return
        assignments = {}
        # Nếu có assignments.json thì load, còn không thì bỏ qua
        if os.path.exists(assignments_path):
            with open(assignments_path, "r", encoding="utf-8") as f:
                assignments = json.load(f)

        # 1. Quét toàn bộ asset thật sự có trong folder (và các subfolder)
        real_asset_set = set()
        for root, dirs, files in os.walk(asset_folder):
            for f in files:
                if f.lower().endswith(('.fbx', '.obj')):
                    asset_name = os.path.splitext(f)[0]
                    real_asset_set.add(asset_name)

        # 2. Lọc assignments: chỉ giữ key còn file
        cleaned_assignments = {k: v for k, v in assignments.items() if k in real_asset_set}

        # 3. Thêm asset mới chưa có vào assignments với value mặc định
        for asset in real_asset_set:
            if asset not in cleaned_assignments:
                cleaned_assignments[asset] = default_category

        # 4. Ghi lại assignments nếu khác bản gốc
        if cleaned_assignments != assignments:
            with open(assignments_path, "w", encoding="utf-8") as f:
                json.dump(cleaned_assignments, f, indent=4)

        return cleaned_assignments



    # --------- Tree Folder  -----------
    @staticmethod
    def get_tree_folder_json_path():
        """Trả về đường dẫn tới tree_folder.json"""
        return os.path.normpath(os.path.join(os.path.dirname(__file__), "tree_folder.json"))

    @staticmethod
    def set_tree_folder():
        """
        Đệ quy quét tất cả các folder bên trong asset_library_path,
        lưu danh sách vào tree_folder.json theo dạng:
        { "tree_folder_list": [<folder1>, <folder2>, ...] }
        """
        asset_folder = Configuration.get_asset_library_path()
        if not asset_folder or not os.path.isdir(asset_folder):
            return False

        folder_list = []
        for root, dirs, files in os.walk(asset_folder):
            # Lưu lại tất cả folder, kể cả root
            folder_list.append(os.path.normpath(root))
        # Ghi ra tree_folder.json
        tree_folder_path = Configuration.get_tree_folder_json_path()
        with open(tree_folder_path, "w", encoding="utf-8") as f:
            json.dump({"tree_folder_list": folder_list}, f, indent=4)
        return True

    @staticmethod
    def get_tree_folder():
        """
        Đọc tree_folder.json và trả về list folder đã lưu.
        Nếu chưa có thì trả về []
        """
        tree_folder_path = Configuration.get_tree_folder_json_path()
        if not os.path.exists(tree_folder_path):
            return []
        try:
            with open(tree_folder_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("tree_folder_list", [])
        except Exception:
            return []
