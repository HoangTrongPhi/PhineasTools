### 30/10/2024
### HOANG TRONG PHI     @HuangFei
### working all

import maya.cmds as cmds
import maya.mel as mel
import os
import subprocess
import sys


####################
#   # ------------------------- HÀM CHÍNH -------------------------
# Hàm trả về file hiện tại của Scene (file đang bật), extension (phần mở rộng) có thể là .ma  hoặc .mb
# vd path là C:/Projects/myScene.ma,   Python sẽ trả về  'myScene.ma'
def GetSceneNameWithExt():
    sceneNameWithExt = cmds.file(query=True, sceneName=True, shortName=True)
    return sceneNameWithExt if sceneNameWithExt else None
#print(GetSceneNameWithExt())

# ------------------------- HÀM CON -------------------------
# Không nhận filePath làm input --> hoạt động trực tiếp với scene hiện tại
# Trả về chỉ phần mở rộng 'ma', 'mb', 'fbx',...
# Phụ thuộc vào GetSceneNameWithExt ()
def GetExtension():
    sceneNameWithExt = GetSceneNameWithExt()
    if sceneNameWithExt:
        return sceneNameWithExt.split('.')[-1]
    return None

# Hàm trả về only tên file scene
def GetSceneName():
    sceneNameWithExt = GetSceneNameWithExt()
    if sceneNameWithExt:
        sceneName = sceneNameWithExt.split('.')[0]
    else:
        sceneName = None
    return sceneName

# Hàm trả về full Path
def GetScenePath():
    sceneNameWithExt = GetSceneNameWithExt()
    if not sceneNameWithExt:
        return None
    return cmds.file(query =True, sceneName=True).replace(sceneNameWithExt, '')

#------------------------------------------------------------------#

# Hàm check xem scene đã tồn tại hay chưa, nếu chưa, confirmDialog
def CheckValidScene(showDialog=True):
    scene = cmds.file(query=True, sceneName=True, shortName=True)
    if not scene:
        if showDialog:
            cmds.confirmDialog(title="Warning",
                               message="Bạn chưa lưu file!",
                               button=["Confirm"])
        return False
    return True


##############################################
#               EXPLORE PATH
##############################################

def browseFolderPath():
    path = ''
    scenePath = GetScenePath()
    if scenePath:
        scenePath = ''
    multipleFilters = 'All Files (*.*)'

    pathList = cmds.fileDialog2(
        fileMode=3,
        startingDirectory=scenePath,
        fileFilter=multipleFilters,
        dialogStyle=2,
        caption = "Chọn Thư Mục"
    ) or []

    if pathList:
        print(pathList[0])
        return pathList[0]
    else:
        return ''

# ---------open Explore---------------
def openExplore():
    if not CheckValidScene():
        return  # Thoát nếu scene chưa được lưu
    folderPath = browseFolderPath()
    print(folderPath)
    if folderPath:
        os.startfile(folderPath)  # Mở thư mục trong File Explorer
        return folderPath

#----------Nhận Path thủ công----------
def getFolderPath(path_text):
    folderPath = path_text.strip()    # strip() loại bỏ khoảng trắng
    if folderPath and os.path.exists(folderPath):
        return folderPath
    else:
        cmds.confirmDialog(title="Error",
                           message="Đường dẫn không hợp lệ!,"
                                   "\nLưu vào Save Scene Path",
                           button=["Confirm Export"])
        return False


# ---------folder Explore---------------
def folderExploreBrowser(path):
    """
    Mở folder cuối cùng của một đường dẫn trong Explorer (Windows) / Finder (Mac)

    Args:
        path (str): đường dẫn file hoặc folder
    """

    if not path:
        return

    # Normalize path
    path = os.path.normpath(path)

    # Nếu là file → lấy folder chứa nó
    if os.path.isfile(path):
        path = os.path.dirname(path)

    # Nếu không tồn tại → thoát
    if not os.path.exists(path):
        print("Path không tồn tại:", path)
        return

    try:
        if sys.platform == "win32":
            subprocess.Popen(f'explorer "{path}"')
        elif sys.platform == "darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    except Exception as e:
        print("Không mở được folder:", e)