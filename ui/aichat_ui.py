# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aichat_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatMainWindow(object):
    def setupUi(self, ChatMainWindow):
        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.resize(500, 350)
        ChatMainWindow.setStyleSheet("#frame\n"
"{\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(251,102,102, 220), stop:1 rgba(20,196,188, 230));\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.contactList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.contactList.sizePolicy().hasHeightForWidth())
        self.contactList.setSizePolicy(sizePolicy)
        self.contactList.setMaximumSize(QtCore.QSize(140, 16777215))
        self.contactList.setStyleSheet("#contactList\n"
"{\n"
"    font: 10 7pt \'微软雅黑 Light\';\n"
"    color: rgb(31,31,31);\n"
"    padding-left:5px; \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(20,196,188);\n"
"    /*border-radius:10px;*/\n"
"}")
        self.contactList.setObjectName("contactList")
        self.horizontalLayout.addWidget(self.contactList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chatDisplay = QtWidgets.QTextEdit(self.centralwidget)
        self.chatDisplay.setStyleSheet("#chatDisplay\n"
"{\n"
"    font: 10 7pt \'微软雅黑 Light\';\n"
"    color: rgb(31,31,31);\n"
"    padding-left:5px; \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(20,196,188);\n"
"    /*border-radius:10px;*/\n"
"}")
        self.chatDisplay.setObjectName("chatDisplay")
        self.verticalLayout.addWidget(self.chatDisplay)
        self.inputEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.inputEdit.sizePolicy().hasHeightForWidth())
        self.inputEdit.setSizePolicy(sizePolicy)
        self.inputEdit.setMaximumSize(QtCore.QSize(16777215, 80))
        self.inputEdit.setStyleSheet("#inputEdit\n"
"{\n"
"    font: 10 7pt \'微软雅黑 Light\';\n"
"    color: rgb(31,31,31);\n"
"    padding-left:5px; \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(20,196,188);\n"
"    /*border-radius:10px;*/\n"
"}")
        self.inputEdit.setObjectName("inputEdit")
        self.verticalLayout.addWidget(self.inputEdit)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setStyleSheet("QPushButton\n"
"{\n"
"    font: 10 7pt \'微软雅黑\';\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(20,196,188);\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(22,218,208);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(17,171,164);\n"
"}")
        self.sendButton.setObjectName("sendButton")
        self.verticalLayout.addWidget(self.sendButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        ChatMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChatMainWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)

    def retranslateUi(self, ChatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatMainWindow.setWindowTitle(_translate("ChatMainWindow", "微信AI智能伙伴"))
        self.sendButton.setText(_translate("ChatMainWindow", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ChatMainWindow()
    ui.setupUi(ChatMainWindow)
    ChatMainWindow.show()
    sys.exit(app.exec_())

