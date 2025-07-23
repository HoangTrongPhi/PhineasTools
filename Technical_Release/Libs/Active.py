import maya.cmds as cmds
import json
import os

def export_active_plugins_to_json(output_dir=r'C:\tempMaya\Plug_in_info\Active'):
    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lấy tất cả plugin (có thể đã được cài)
    all_plugins = cmds.pluginInfo(query=True, listPlugins=True) or []

    plugin_data = []

    for plugin in all_plugins:
        try:
            loaded = cmds.pluginInfo(plugin, query=True, loaded=True)
            autoload = cmds.pluginInfo(plugin, query=True, autoload=True)

            if loaded or autoload:
                info = {
                    'name': plugin,
                    'path': cmds.pluginInfo(plugin, query=True, path=True) or "Unknown",
                    'loaded': loaded,
                    'autoLoad': autoload
                }
                plugin_data.append(info)

        except RuntimeError:
            # Plugin không thể truy vấn (bị lỗi, thiếu file...) thì bỏ qua
            pass

    # Ghi ra file JSON
    output_file = os.path.join(output_dir, 'plugin_info_active.json')
    with open(output_file, 'w') as f:
        json.dump(plugin_data, f, indent=4)

    print(f"Đã ghi plugin đang loaded hoặc autoLoad tại: {output_file}")
export_active_plugins_to_json()


def toggle_plugins_from_json(mode):
    json_file = r'C:\tempMaya\Plug_in_info\Active\plugin_info_active.json'

    if not os.path.exists(json_file):
        cmds.warning(f"File không tồn tại: {json_file}")
        return

    # Đọc dữ liệu từ file JSON
    with open(json_file, 'r') as f:
        plugins = json.load(f)

    for plugin in plugins:
        plugin_name = plugin['name']
        try:
            if mode == 1:
                # Nếu plugin đang loaded, thì unload
                if cmds.pluginInfo(plugin_name, query=True, loaded=True):
                    cmds.unloadPlugin(plugin_name, force=True)
                    print(f"🔌 Đã tắt: {plugin_name}")
            elif mode == 2:
                # Nếu plugin chưa loaded, thì load
                if not cmds.pluginInfo(plugin_name, query=True, loaded=True):
                    cmds.loadPlugin(plugin_name)
                    print(f"Đã bật: {plugin_name}")
        except RuntimeError as e:
            print(f"Không thể xử lý plugin {plugin_name}: {e}")

