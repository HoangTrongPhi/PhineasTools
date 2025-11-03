import os
import sys
import glob
import shutil
import json

# ---- 1. Đặt đường dẫn gốc, khai báo các biến sử dụng ----
RELEASE_PATH = r"C:/PhineasTools/Technical_Release"

ICON_PATH = os.path.join(RELEASE_PATH, "_Icons")
COMMON_PATH = os.path.join(RELEASE_PATH, "Common/Python")
MAYA_TOOLSETS_PATH = os.path.join(RELEASE_PATH, "Software/Maya/Toolsets")

# ---- 2. Update/cộng nối các biến môi trường cho Maya ----
def update_envs():
    # Maya script path (dùng để Maya load các toolsets tự động)
    current_maya_script_path = os.environ.get("MAYA_SCRIPT_PATH", "")
    if MAYA_TOOLSETS_PATH not in current_maya_script_path:
        new_maya_script_path = (current_maya_script_path + ";" + MAYA_TOOLSETS_PATH).strip(";")
        os.environ["MAYA_SCRIPT_PATH"] = new_maya_script_path

    # XBMLANGPATH cho icon Maya
    current_xbmlang_path = os.environ.get("XBMLANGPATH", "")
    if ICON_PATH not in current_xbmlang_path:
        new_xbmlang_path = (current_xbmlang_path + ";" + ICON_PATH).strip(";")
        os.environ["XBMLANGPATH"] = new_xbmlang_path

    # Thêm sys.path để import các module custom Python
    if RELEASE_PATH not in sys.path:
        sys.path.append(RELEASE_PATH)

    print(f"[INFO] Da set xong MayaTools Path: {MAYA_TOOLSETS_PATH}")

# ---- 3. Tự động copy icons và shelves  ----
def check_path(path):
    if os.path.exists(path):
        return True
    else:
        os.makedirs(path, exist_ok=True)
        return False

def copy_files(src_pattern, dst_folder):
    files = glob.glob(src_pattern)
    for file in files:
        if os.path.isfile(file):
            shutil.copy(file, dst_folder)

def copy_icons_and_shelves():
    try:
        import maya.cmds as cmds
        user_pref_dir = cmds.internalVar(userPrefDir=True)
    except ImportError:
        user_pref_dir = os.path.expanduser('~/Documents/maya/')
    icon_path = os.path.join(user_pref_dir, "icons")
    shelf_path = os.path.join(user_pref_dir, "shelves")

    print("[INFO] - Checking folder path...")
    check_path(icon_path)
    check_path(shelf_path)

    print("[INFO] - Copying icons...")
    icon_src = os.path.join(RELEASE_PATH, "_icons", "*")
    copy_files(icon_src, icon_path)

    print("[INFO] - Copying shelf...")
    shelf_src = os.path.join(RELEASE_PATH, "Software", "Maya", "Data", "Shelves", "*")
    copy_files(shelf_src, shelf_path)

    print("[INFO] - Done copy icons/shelves.")

# ---- 4. Quét và lưu các environment path liên quan vào RELEASE_PATH.txt ----
def get_env_paths():
    env_vars = ["PYTHONPATH", "MAYA_MODULE_PATH", "MAYA_SCRIPT_PATH", "XBMLANGPATH"]
    env_paths = {}
    for var in env_vars:
        val = os.environ.get(var)
        if val:
            sep = ';' if os.name == 'nt' else ':'
            # Chỉ lấy path tồn tại
            paths = [p for p in val.split(sep) if p and os.path.exists(p)]
            if paths:
                env_paths[var] = paths
    # Thêm custom path (toolset, common, icons) nếu chưa có
    if "CUSTOM_PATHS" not in env_paths:
        env_paths["CUSTOM_PATHS"] = []
    for p in [RELEASE_PATH, COMMON_PATH, MAYA_TOOLSETS_PATH, ICON_PATH]:
        if p not in env_paths["CUSTOM_PATHS"] and os.path.exists(p):
            env_paths["CUSTOM_PATHS"].append(p)
    return env_paths

def save_release_path_info():
    try:
        import maya.cmds as cmds
        script_folder = cmds.internalVar(userScriptDir=True)
    except ImportError:
        script_folder = os.path.expanduser('~/Documents/maya/scripts/')
    save_path = os.path.join(script_folder, "PHINEASTOOL_PATH.txt")
    env_paths = get_env_paths()
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(env_paths, f, ensure_ascii=False, indent=4)
    print(f"[INFO] - RELEASE_PATH info saved to {save_path}")

# ---- 5. Hàm main để kết hợp các bước ----
def main():
    print(f"[INFO] Maya Toolsets Path: {MAYA_TOOLSETS_PATH}")
    update_envs()
    copy_icons_and_shelves()
    save_release_path_info()

# ---- 6. Hỗ trợ drag & drop trong Maya ----
def onMayaDroppedPythonFile(*args, **kwargs):
    main()
    print("[INFO] - INSTALL hoàn tất! Khởi động lại Maya để chạy Tools.")

if __name__ == "__main__":
    main()
