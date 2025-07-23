import os
import json
from collections import defaultdict

class File_JSON_Utils:
    @staticmethod
    def read_json(path):
        """
        Đọc nội dung từ file JSON và trả về dạng dict hoặc list.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Không tìm thấy file: {path}")
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def write_json(path, data, indent=4):
        """
        Ghi dữ liệu Python (dict/list) vào file JSON.
        """
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)

    @staticmethod
    def ensure_dir_exists(path):
        """
        Tạo thư mục (và các thư mục cha nếu cần). Không lỗi nếu đã tồn tại.
        """
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def classify_by_key(data, key):
        """
        Phân loại các đối tượng trong list theo giá trị của một key.
        Trả về dict: { value: [objects...] }
        """
        if not isinstance(data, list):
            raise ValueError("Dữ liệu phải là một list chứa các dict.")

        classified = defaultdict(list)
        for item in data:
            if not isinstance(item, dict):
                continue
            value = item.get(key, None)
            classified[value].append(item)

        return dict(classified)

    @staticmethod
    def classify_by_keys(data, keys):
        """
        Phân loại lồng theo nhiều key.
        Trả về dict lồng dạng:
        {
            key1_value: {
                key2_value: [...],
                ...
            },
            ...
        }
        """
        if not isinstance(data, list):
            raise ValueError("Dữ liệu phải là một list chứa các dict.")
        if not keys:
            raise ValueError("Danh sách keys không được rỗng.")

        def recursive_classify(items, remaining_keys):
            if not remaining_keys:
                return items  # Đạt cấp cuối cùng → trả danh sách object

            current_key = remaining_keys[0]
            grouped = defaultdict(list)

            for item in items:
                if not isinstance(item, dict):
                    continue
                value = item.get(current_key, None)
                grouped[value].append(item)

            return {
                key: recursive_classify(grouped[key], remaining_keys[1:])
                for key in grouped
            }

        return recursive_classify(data, keys)
