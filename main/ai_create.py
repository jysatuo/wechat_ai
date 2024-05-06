# -*-coding:utf-8 -*-

from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.ai_create_ui import *
import os
import shutil
import json
import time
import random


class CreateRole(QtWidgets.QDialog, Ui_AICharacterCreation):
    refresh_signal = pyqtSignal(dict, list, int)

    def __init__(self, filepath: str, ai: dict = {}, n: int = -1):
        super(CreateRole, self).__init__()
        self.setupUi(self)
        self.filepath = filepath
        self.ai = ai  # 没有传入就是创建，传入就是对原有数据进行修改
        self.n = n
        if ai:
            image = QImage(ai["avatar"])
            image = image.scaled(self.avatarLabel.size(), Qt.KeepAspectRatio)
            self.avatarLabel.setScaledContents(True)
            self.avatarLabel.setPixmap(QPixmap.fromImage(image))
            self.nameLineEdit.setText(ai["name"])
            self.descLineEdit.setText(ai["describe"]) 
            self.promptEdit.setText(ai["prompt"])
            self.slider1.setValue(ai["Output Length"])
            self.label1.setText(str(ai["Output Length"]))
            self.slider2.setValue(ai["Temperature"] * 10)
            self.label2.setText(str(ai["Temperature"]))
            self.slider3.setValue(ai["Top-P"] * 10)
            self.label3.setText(str(ai["Top-P"]))
            self.slider4.setValue(ai["Top-K"])
            self.label4.setText(str(ai["Top-K"]))
            self.slider5.setValue(ai["Repetition Penalty"] * 100)
            self.label5.setText(str(ai["Repetition Penalty"]))
            self.save_file = ai["avatar"]
        else:
            self.save_file = ""
        self.avatarButton.clicked.connect(self.load_avatar)
        self.createButton.clicked.connect(self.create)
        self.slider1.valueChanged.connect(self.valueChanged1)
        self.slider2.valueChanged.connect(self.valueChanged2)
        self.slider3.valueChanged.connect(self.valueChanged3)
        self.slider4.valueChanged.connect(self.valueChanged4)
        self.slider5.valueChanged.connect(self.valueChanged5)
        self.cancelButton.clicked.connect(self.close)

    def valueChanged1(self, value):
        self.label1.setText(str(value))

    def valueChanged2(self, value):
        self.label2.setText(str(value / 10))

    def valueChanged3(self, value):
        self.label3.setText(str(value / 10))

    def valueChanged4(self, value):
        self.label4.setText(str(value))

    def valueChanged5(self, value):
        self.label5.setText(str(value / 100))

    def create(self):
        if not self.avatarLabel.pixmap():
            QMessageBox.critical(self, '失败', '请先上传图片')
        elif not self.nameLineEdit.text():
            QMessageBox.critical(self, '失败', '请先编辑名称')
        elif not self.promptEdit.toPlainText():
            QMessageBox.critical(self, '失败', '请先编辑prompt(提示词)')
        else:
            if not self.ai:
                msgid = str(int(time.time()))+str(random.randint(1000,9999))    # 防止重复
                model_param = {"Output Length": self.slider1.value(), "Temperature": self.slider2.value() / 10,
                               "Top-P": self.slider3.value() / 10, "Top-K": self.slider4.value(),
                               "Repetition Penalty": self.slider5.value() / 100, "avatar": self.save_file,
                               "name": self.nameLineEdit.text(), "describe": self.descLineEdit.text(), 
                               "prompt": self.promptEdit.toPlainText(), "msgid": msgid}
                filename = f"{self.filepath}/config.conf"
                if os.path.isfile(filename):
                    with open(filename, 'r') as file:
                        array_str = file.read()
                        if len(array_str):
                            array = json.loads(array_str)
                        else:
                            array = []
                        array.append(model_param)
                    with open(filename, "w") as f:
                        json.dump(array, f)
                else:
                    with open(filename, 'w') as f:
                        json.dump([model_param], f)
                # 创建当前AI角色的messages  
                messages_path = f"{self.filepath}/messages"
                if not os.path.exists(messages_path):
                    os.makedirs(messages_path)    
                msg_file = f"{messages_path}/{msgid}.json"
                with open(msg_file, "w") as f:
                    json.dump([{"role": "system", "content": model_param["prompt"]}], f)         
            else:
                model_param = {"Output Length": self.slider1.value(), "Temperature": self.slider2.value() / 10,
                               "Top-P": self.slider3.value() / 10, "Top-K": self.slider4.value(),
                               "Repetition Penalty": self.slider5.value() / 100, "avatar": self.save_file,
                               "name": self.nameLineEdit.text(), "describe": self.descLineEdit.text(),
                               "prompt": self.promptEdit.toPlainText(), "msgid": self.ai["msgid"]}
                filename = f"{self.filepath}/config.conf"
                with open(filename, 'r') as file:
                    array_str = file.read()
                    array = json.loads(array_str)
                    array[self.n] = model_param
                with open(filename, 'w') as f:
                    json.dump(array, f)
                msg_file = f"{self.filepath}/messages/{model_param['msgid']}.json"
                if os.path.isfile(msg_file):                
                    with open(msg_file, 'r') as file:
                        array_str = file.read()
                        array = json.loads(array_str)
                        array[0]["content"] = model_param["prompt"]              
                    with open(msg_file, "w") as f:
                        json.dump(array, f)   
                else:
                    array = [{"role":"system", "content":model_param["prompt"]}]
                    with open(msg_file, "w") as f:
                        json.dump(array, f)
            self.refresh_signal.emit(model_param, array, self.n)            
            self.accept()

    def load_avatar(self):
        image_file, _ = QFileDialog.getOpenFileName(self, '选择图片', '', 'Images (*.jpg *.png *.ico)')
        if image_file:
            image = QImage(image_file)
            image = image.scaled(self.avatarLabel.size(), Qt.KeepAspectRatio)
            self.avatarLabel.setScaledContents(True)
            self.avatarLabel.setPixmap(QPixmap.fromImage(image))
            suffix = image_file.split('/')[-1]
            ## 设置保存的文件夹路径和文件名
            folder_path = f"{self.filepath}/ai_avatar"
            save_file = f'{folder_path}/{suffix}'
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            self.save_file = save_file
            try:
                shutil.copy(image_file, save_file)
                QMessageBox.information(self, '成功', '图片上传成功！')
            except Exception as e:
                QMessageBox.critical(self, '失败', f'图片上传失败：{e}')

    def close(self):
        self.accept()
