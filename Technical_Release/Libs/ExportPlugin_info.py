import maya.cmds as cmds
import json
import os



def export_all_plugins_status_to_json(output_dir = r'C:\tempMaya\Plug_in_info\All'):
    # Tạo thư mục nếu chưa tồn tại
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Lấy tất cả plugin hiện có mặt trong Maya (load hoặc không)
    all_plugins = cmds.pluginInfo(query=True, listPlugins=True) or []

    plugin_data = []

    for plugin in all_plugins:
        try:
            info = {
                'name': plugin,
                'path': cmds.pluginInfo(plugin, query=True, path=True) or "Unknown",
                'loaded': cmds.pluginInfo(plugin, query=True, loaded=True),
                'autoLoad': cmds.pluginInfo(plugin, query=True, autoload=True)
            }
        except RuntimeError:
            info = {
                'name': plugin,
                'path': "Unknown",
                'loaded': False,
                'autoLoad': False
            }

        plugin_data.append(info)

    # Ghi ra file JSON
    output_file = os.path.join(output_dir, 'plugin_info_all.json')
    with open(output_file, 'w') as f:
        json.dump(plugin_data, f, indent=4)
    print(f"Đã ghi toàn bộ plugin vào: {output_file}")

export_all_plugins_status_to_json()