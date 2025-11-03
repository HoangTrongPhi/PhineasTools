import importlib
import sys
import os

def onMayaDroppedPythonFile(*args):
    scripts_path = os.path.join(os.environ.get('USERPROFILE', ''), 'Documents', 'maya', 'scripts', 'mtTools')
    
    if scripts_path not in sys.path:
        sys.path.append(scripts_path)

    try:
        import mtTools.mtTools as mtTools
        importlib.reload(mtTools)
        mtTools.showUI()
        mtTools.shelf.Start()  # Remove this line if you don't want the shelf
    except Exception as e:
        import traceback
        print("Error loading mtTools:", traceback.format_exc())
