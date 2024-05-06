# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ai_playground_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChatMainWindow(object):
    def setupUi(self, ChatMainWindow):
        ChatMainWindow.setObjectName("ChatMainWindow")
        ChatMainWindow.resize(596, 343)
        ChatMainWindow.setStyleSheet("#frame\n"
"{\n"
"     background-color:rgb(255, 170, 0);\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ChatMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.settingList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.settingList.sizePolicy().hasHeightForWidth())
        self.settingList.setSizePolicy(sizePolicy)
        self.settingList.setMaximumSize(QtCore.QSize(140, 16777215))
        self.settingList.setStyleSheet("#settingList\n"
"{\n"
"    font: 10 7pt \'微软雅黑 Light\';\n"
"    color: rgb(31,31,31);\n"
"    padding-left:5px; \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(20,196,188);\n"
"    /*border-radius:10px;*/\n"
"}")
        self.settingList.setObjectName("settingList")
        self.verticalLayout_2.addWidget(self.settingList)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("QComboBox\n"
"{\n"
"    font: 25 12pt \'微软雅黑\';\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(20,196,188);\n"
"    border:none;\n"
"}\n"
"\n"
"QComboBox:pressed\n"
"{\n"
"    background-color: rgb(17,171,164);\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 18))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    font: 25 12pt \'微软雅黑\';\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 3, 2, 1)
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
        self.gridLayout.addWidget(self.contactList, 1, 1, 2, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(288, 18))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 18))
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setStyleSheet("stackedWidget {\n"
"    padding: 0px;\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    margin:0px;\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setMinimumSize(QtCore.QSize(258, 18))
        self.page.setAutoFillBackground(True)
        self.page.setStyleSheet("page {\n"
"    padding: 0px;\n"
"    width: 100%;\n"
"    height: 100%;\n"
"    margin:0px;\n"
"}")
        self.page.setObjectName("page")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sendButton_2 = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton_2.sizePolicy().hasHeightForWidth())
        self.sendButton_2.setSizePolicy(sizePolicy)
        self.sendButton_2.setMinimumSize(QtCore.QSize(0, 18))
        self.sendButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    font: 25 12pt \'微软雅黑\';\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(20,196,188);\n"
"    border:none;\n"
"    margin:0px;\n"
"    padding:0px;\n"
"    height:100%;\n"
"    width:100%;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color: rgb(22,218,208);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: rgb(17,171,164);\n"
"}")
        self.sendButton_2.setObjectName("sendButton_2")
        self.horizontalLayout.addWidget(self.sendButton_2)
        self.pushFileButton = QtWidgets.QPushButton(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushFileButton.sizePolicy().hasHeightForWidth())
        self.pushFileButton.setSizePolicy(sizePolicy)
        self.pushFileButton.setMinimumSize(QtCore.QSize(0, 18))
        self.pushFileButton.setStyleSheet("")
        self.pushFileButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ui/file-import.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushFileButton.setIcon(icon)
        self.pushFileButton.setIconSize(QtCore.QSize(18, 18))
        self.pushFileButton.setFlat(True)
        self.pushFileButton.setObjectName("pushFileButton")
        self.horizontalLayout.addWidget(self.pushFileButton)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.page_2.setAutoFillBackground(True)
        self.page_2.setStyleSheet("page_2 {\n"
"    padding: 0px;\n"
"    width: 100%;\n"
"    height: 100%;\n"
"}")
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sendButton = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QtCore.QSize(0, 18))
        self.sendButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sendButton.setAutoFillBackground(False)
        self.sendButton.setStyleSheet("QPushButton\n"
"{\n"
"    font: 25 12pt \'微软雅黑\';\n"
"    color: rgb(255,255,255);\n"
"    background-color: rgb(20,196,188);\n"
"    border:none;\n"
"    margin: 0px; \n"
"    padding: 0px;\n"
"    width: 100%;\n"
"    height: 100%;\n"
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
        self.horizontalLayout_2.addWidget(self.sendButton)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.chatDisplay = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        self.chatDisplay.setFont(font)
        self.chatDisplay.setStyleSheet("#chatDisplay\n"
"{\n"
"    font: 15 7pt \'微软雅黑 Light\';\n"
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
        self.inputEdit.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(False)
        self.inputEdit.setFont(font)
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
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        ChatMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChatMainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ChatMainWindow)

    def retranslateUi(self, ChatMainWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatMainWindow.setWindowTitle(_translate("ChatMainWindow", "微信AI智能伙伴"))
        self.pushButton_2.setText(_translate("ChatMainWindow", "Create Role"))
        self.sendButton_2.setText(_translate("ChatMainWindow", "Send"))
        self.sendButton.setText(_translate("ChatMainWindow", "Send"))
        self.chatDisplay.setHtml(_translate("ChatMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑 Light\'; font-size:7pt; font-weight:15; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:25;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatMainWindow = QtWidgets.QMainWindow()
    ui = Ui_ChatMainWindow()
    ui.setupUi(ChatMainWindow)
    ChatMainWindow.show()
    sys.exit(app.exec_())

