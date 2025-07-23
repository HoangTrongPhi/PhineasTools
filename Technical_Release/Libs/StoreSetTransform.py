"""
Author: Hoang Trong Phi -@HuangFei
Update 3/11/2024
Update 6/13/2025
"""
from maya import cmds
import os, json
tempFolder = 'C:\\tempMaya\storeTransform'
# tạo một đường dẫn hoàn chỉnh
DIRECTORY = os.path.join(tempFolder, 'transform')

# Class kế thừa (dict) cho phép mỗi object của class này hoạt động như một dictionary thông thường ( JSON)
# Việc này giúp lưu trữ, truy cập dữ liệu đơn giản hơn
class StoreSetTransform(dict):

    def __init__(self):
        super(StoreSetTransform, self).__init__()
    # Check và tạo Directory
    def createDir(self, directory=DIRECTORY):
        if not os.path.exists(directory):
            print (directory)
            os.makedirs(directory)

    def getTransform(self, obj):
        """
            Args:
                obj: obj name
                transform: transform data bao gồm translate, rotate, scale thành JSON
        """
        transform = {}
        objInfo = {}

        translateX = cmds.getAttr(('{}.translateX').format(obj))
        translateY = cmds.getAttr(('{}.translateY').format(obj))
        translateZ = cmds.getAttr(('{}.translateZ').format(obj))
        translateObj = [translateX, translateY, translateZ]
        transform['Translate'] = translateObj

        rotateX = cmds.getAttr(('{}.rotateX').format(obj))
        rotateY = cmds.getAttr(('{}.rotateY').format(obj))
        rotateZ = cmds.getAttr(('{}.rotateZ').format(obj))
        rotateObj = [rotateX, rotateY, rotateZ]
        transform['Rotate'] = rotateObj

        scaleX = cmds.getAttr(('{}.scaleX').format(obj))
        scaleY = cmds.getAttr(('{}.scaleY').format(obj))
        scaleZ = cmds.getAttr(('{}.scaleZ').format(obj))
        scaleObj = [scaleX, scaleY, scaleZ]
        transform['Scale'] = scaleObj

        objInfo[obj] = transform
        return objInfo

    def writeAllTransformtoJSON(self, fileName, directory=DIRECTORY):
        self.createDir(directory)
        infoJsonFile = os.path.join(directory, ('{}.json').format(fileName))
        transformNodes = cmds.ls(type='transform', long=True)


        """
        1. with kích hoạt "Context Manager" (trình quản lý ngữ cảnh) thiết lập môi trường tạm thời, clean sau khi môi trường kết thúc
        2. 'w' đây là mode ghi ( write), nếu file chưa tồn tại, nó sẽ tạo một file mới.
            note: các mode khác  'r' (read), 'a' (append - ghi tiếp vào cuối file mà ko xóa nội dung cũ), 
            'b' (binary- cho các file ko phải dạng văn bản như hình ảnh, video,...)
        3. as f:
        - Hàm open(...) return (file object). Giống như remote điều khiển, cho phép user tương tác với file
        - as f gán đối tượng cho một biến có tên f (as file_handle, as my_file,....) nhưng thường đặt là f cho gọn
        - json.dump (sử dụng thư viện json để ghi (dump) dữ liệu vào ( f )
        """
        with open(infoJsonFile, 'w') as f:
            for node in transformNodes:
                objInfo = self.getTransform(node)
                self.update(objInfo)

            json.dump(self, f, indent=4)
        return 1

    # dưới đây cũng tương tự nhưng mà là đọc (read)
    def readTransformsFromJSON(self, fileName, directory=DIRECTORY):
        if not os.path.exists(directory):
            return 0
        files = os.listdir(directory)
        jsonFiles = [f for f in files if f.endswith('.json')]
        fileNameJson = fileName + '.json'
        if fileNameJson in jsonFiles:
            infoJsonFile = os.path.join(directory, fileNameJson)
            with open(infoJsonFile, 'r') as f:
                data = json.load(f)
        else:
            data = {}
        self[fileName] = data

    # lưu ý đối tượng là fileName nhưng thực ra nó là sceneName ( tên scene được lưu)
    def applyTransform(self, fileName, directory=DIRECTORY):
        mess = 'Do you want to ReStore Transform?'
        confirm = cmds.confirmDialog(title='Confirm Dialog', message=mess, button=['Yes', 'No'], defaultButton='Yes',
                                     cancelButton='No', dismissString='No')

        if confirm == 'Yes':
            excludeNodes = ['|persp', '|top', '|front', '|side']
            transformNodes = cmds.ls(type='transform', long=True)
            self.readTransformsFromJSON(fileName, directory)

            if self[fileName] == {}:
                cmds.confirmDialog(
                    message='Khong tim thay transform cua scene {}, Vui long kiem tra lai'.format(fileName))
                return 0

            for node in transformNodes:
                if node not in excludeNodes:
                    try:
                        cmds.setAttr('{}.translateX'.format(node), self[fileName][node]['Translate'][0])
                        cmds.setAttr('{}.translateY'.format(node), self[fileName][node]['Translate'][1])
                        cmds.setAttr('{}.translateZ'.format(node), self[fileName][node]['Translate'][2])
                        cmds.setAttr('{}.rotateX'.format(node), self[fileName][node]['Rotate'][0])
                        cmds.setAttr('{}.rotateY'.format(node), self[fileName][node]['Rotate'][1])
                        cmds.setAttr('{}.rotateZ'.format(node), self[fileName][node]['Rotate'][2])
                        cmds.setAttr('{}.scaleX'.format(node), self[fileName][node]['Scale'][0])
                        cmds.setAttr('{}.scaleY'.format(node), self[fileName][node]['Scale'][1])
                        cmds.setAttr('{}.scaleZ'.format(node), self[fileName][node]['Scale'][2])
                    except:
                        pass

            #Xóa file JSON sau khi áp dụng xong
            json_path = os.path.join(directory, fileName + ".json")
            if os.path.exists(json_path):
                try:
                    os.remove(json_path)
                    print("Đã xóa file JSON:", json_path)
                except Exception as e:
                    print("Không thể xóa file:", e)

        return 1
