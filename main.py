# -*- coding: utf-8 -*-

"""
Created By zhongweisheng1
"""

import sys, configparser, threading, os, time
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon("./icon.ico"))
        Form.resize(800, 500)
        Form.setMinimumSize(QtCore.QSize(800, 500))
        Form.setMaximumSize(QtCore.QSize(800, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        Form.setFont(font)
        Form.setStyleSheet("#Form{\n"
"    background-color: white;\n"
"}")
        self.Z_1 = QtWidgets.QFrame(Form)
        self.Z_1.setGeometry(QtCore.QRect(0, 0, 210, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Z_1.setFont(font)
        self.Z_1.setStyleSheet("#Z_1{\n"
"    background-color: #4ABDAC;\n"
"}")
        self.Z_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Z_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Z_1.setObjectName("Z_1")
        self.Z_2 = QtWidgets.QFrame(self.Z_1)
        self.Z_2.setGeometry(QtCore.QRect(10, 10, 190, 51))
        self.Z_2.setObjectName("Z_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Z_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Z_5 = QtWidgets.QLabel(self.Z_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.Z_5.setFont(font)
        self.Z_5.setStyleSheet("color: white;")
        self.Z_5.setObjectName("Z_5")
        self.horizontalLayout.addWidget(self.Z_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Z_6 = QtWidgets.QFrame(self.Z_1)
        self.Z_6.setGeometry(QtCore.QRect(10, 70, 190, 370))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Z_6.setFont(font)
        self.Z_6.setStyleSheet("#Z_6{\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"}")
        self.Z_6.setObjectName("Z_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Z_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Z_7 = QtWidgets.QPushButton(self.Z_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Z_7.setFont(font)
        self.Z_7.setStyleSheet("margin: 5px;\n"
"color: #4ABDAC;")
        self.Z_7.setObjectName("Z_7")
        self.verticalLayout.addWidget(self.Z_7)
        self.Z_19 = QtWidgets.QPushButton(self.Z_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Z_19.setFont(font)
        self.Z_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_19.setStyleSheet("background-color: #4ABDAC;\n"
"color: white;\n"
"margin: 10px;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.Z_19.setObjectName("Z_19")
        self.verticalLayout.addWidget(self.Z_19)
        self.Z_20 = QtWidgets.QPushButton(self.Z_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Z_20.setFont(font)
        self.Z_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_20.setStyleSheet("background-color: #4ABDAC;\n"
"color: white;\n"
"margin: 10px;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.Z_20.setObjectName("Z_20")
        self.verticalLayout.addWidget(self.Z_20)
        self.Z_18 = QtWidgets.QPushButton(self.Z_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.Z_18.setFont(font)
        self.Z_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Z_18.setStyleSheet("background-color: #4ABDAC;\n"
"color: white;\n"
"margin: 10px;\n"
"border-radius: 5px;\n"
"padding: 5px;")
        self.Z_18.setObjectName("Z_18")
        self.verticalLayout.addWidget(self.Z_18)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.Z_12 = QtWidgets.QFrame(Form)
        self.Z_12.setEnabled(True)
        self.Z_12.setGeometry(QtCore.QRect(210, 0, 590, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.Z_12.setFont(font)
        self.Z_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Z_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Z_12.setObjectName("Z_12")
        self.Z_9 = QtWidgets.QLabel(self.Z_12)
        self.Z_9.setGeometry(QtCore.QRect(10, 10, 570, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Z_9.setFont(font)
        self.Z_9.setStyleSheet("color: #4ABDAC;")
        self.Z_9.setObjectName("Z_9")
        self.A_IPAddr = QtWidgets.QLineEdit(self.Z_12)
        self.A_IPAddr.setGeometry(QtCore.QRect(30, 60, 440, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_IPAddr.setFont(font)
        self.A_IPAddr.setStyleSheet("border: 1px solid #4ABDAC;\n"
"border-radius: 10px;\n"
"padding-left: 5px;")
        self.A_IPAddr.setInputMask("")
        self.A_IPAddr.setObjectName("A_IPAddr")
        self.A_IPConnect = QtWidgets.QPushButton(self.Z_12)
        self.A_IPConnect.setGeometry(QtCore.QRect(480, 60, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_IPConnect.setFont(font)
        self.A_IPConnect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.A_IPConnect.setStyleSheet("border: 1px solid #4ABDAC;\n"
"background-color: #4ABDAC;\n"
"color: white;\n"
"border-radius: 10px;")
        self.A_IPConnect.setObjectName("A_IPConnect")
        self.A_Devices = QtWidgets.QTableWidget(self.Z_12)
        self.A_Devices.setGeometry(QtCore.QRect(30, 110, 530, 370))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_Devices.setFont(font)
        self.A_Devices.setStyleSheet("QTableWidget{\n"
"    border: 1px solid #4ABDAC;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    background-color: #4ABDAC;\n"
"    border: none;\n"
"    color: white;\n"
"}")
        self.A_Devices.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.A_Devices.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.A_Devices.setGridStyle(QtCore.Qt.SolidLine)
        self.A_Devices.setObjectName("A_Devices")
        self.A_Devices.setColumnCount(3)
        self.A_Devices.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.A_Devices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.A_Devices.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.A_Devices.setHorizontalHeaderItem(2, item)
        self.A_Devices.horizontalHeader().setDefaultSectionSize(176)
        self.A_Devices.verticalHeader().setVisible(False)
        self.Z_13 = QtWidgets.QFrame(Form)
        self.Z_13.setGeometry(QtCore.QRect(210, 0, 590, 500))
        self.Z_13.hide()
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setUnderline(True)
        self.Z_13.setFont(font)
        self.Z_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Z_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Z_13.setObjectName("Z_13")
        self.Z_10 = QtWidgets.QLabel(self.Z_13)
        self.Z_10.setGeometry(QtCore.QRect(10, 10, 570, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Z_10.setFont(font)
        self.Z_10.setStyleSheet("color: #4ABDAC;")
        self.Z_10.setObjectName("Z_10")
        self.A_CommandLine = QtWidgets.QLineEdit(self.Z_13)
        self.A_CommandLine.setGeometry(QtCore.QRect(40, 130, 510, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_CommandLine.setFont(font)
        self.A_CommandLine.setStyleSheet("border: 1px solid #4ABDAC;\n"
"border-radius: 10px;\n"
"padding-left: 5px;")
        self.A_CommandLine.setObjectName("A_CommandLine")
        self.A_Save = QtWidgets.QPushButton(self.Z_13)
        self.A_Save.setGeometry(QtCore.QRect(40, 450, 511, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_Save.setFont(font)
        self.A_Save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.A_Save.setStyleSheet("border: 1px solid #4ABDAC;\n"
"background-color: #4ABDAC;\n"
"color: white;\n"
"border-radius: 10px;")
        self.A_Save.setObjectName("A_Save")
        self.A_Path = QtWidgets.QLineEdit(self.Z_13)
        self.A_Path.setGeometry(QtCore.QRect(40, 60, 510, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.A_Path.setFont(font)
        self.A_Path.setStyleSheet("border: 1px solid #4ABDAC;\n"
"border-radius: 10px;\n"
"padding-left: 5px;")
        self.A_Path.setObjectName("A_Path")
        self.Z_14 = QtWidgets.QLabel(self.Z_13)
        self.Z_14.setGeometry(QtCore.QRect(40, 200, 510, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Z_14.setFont(font)
        self.Z_14.setStyleSheet("color: #4ABDAC;")
        self.Z_14.setObjectName("Z_14")
        self.Z_11 = QtWidgets.QLineEdit(self.Z_13)
        self.Z_11.setGeometry(QtCore.QRect(59, 230, 470, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setUnderline(True)
        self.Z_11.setFont(font)
        self.Z_11.setStyleSheet("color: blue;")
        self.Z_11.setFrame(False)
        self.Z_11.setReadOnly(True)
        self.Z_11.setObjectName("Z_11")
        self.Z_1.raise_()
        self.Z_13.raise_()
        self.Z_12.raise_()
        self.Z_15 = QtWidgets.QFrame(self.Z_1)
        self.Z_15.setObjectName(u"Z_15")
        self.Z_15.setGeometry(QtCore.QRect(10, 449, 191, 41))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Z_15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Z_16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.Z_16)
        self.Z_21 = QtWidgets.QLabel(self.Z_15)
        self.Z_21.setObjectName(u"Z_21")
        font4 = QtGui.QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(9)
        self.Z_21.setFont(font4)
        self.Z_21.setStyleSheet(u"color: white;")
        self.horizontalLayout_2.addWidget(self.Z_21)
        self.Z_17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.Z_17)

        self.retranslateUi(Form)
        self.Z_18.clicked.connect(Form.close)
        self.Z_19.clicked.connect(self.Z_12.show)
        self.Z_19.clicked.connect(self.Z_13.hide)
        self.Z_20.clicked.connect(self.Z_13.show)
        self.Z_20.clicked.connect(self.Z_12.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Scrcpy GUI"))
        self.Z_5.setText(_translate("Form", "Scrcpy GUI"))
        self.Z_7.setText(_translate("Form", "菜单"))
        self.Z_19.setText(_translate("Form", "开始"))
        self.Z_20.setText(_translate("Form", "设置"))
        self.Z_18.setText(_translate("Form", "退出"))
        self.Z_9.setText(_translate("Form", "开始"))
        self.A_IPAddr.setPlaceholderText(_translate("Form", "无线连接"))
        self.A_IPConnect.setText(_translate("Form", "连接"))
        item = self.A_Devices.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.A_Devices.horizontalHeaderItem(1)
        item.setText(_translate("Form", "状态"))
        item = self.A_Devices.horizontalHeaderItem(2)
        item.setText(_translate("Form", "操作"))
        self.Z_10.setText(_translate("Form", "设置"))
        self.A_CommandLine.setPlaceholderText(_translate("Form", "命令行参数"))
        self.A_Save.setText(_translate("Form", "保存"))
        self.A_Path.setPlaceholderText(_translate("Form", "Scrcpy 路径"))
        self.Z_14.setText(_translate("Form", "帮助："))
        self.Z_11.setText(_translate("Form", "https://github.com/Genymobile/scrcpy/blob/master/README.zh-Hans.md"))
        self.Z_21.setText(_translate("Form", "GitHub: zhongweisheng1"))

Flag = True

class App(Ui_Form):
    def __init__(self):
        self.flag = True
        self.Form = QtWidgets.QWidget()

        super().setupUi(self.Form)
        super().retranslateUi(self.Form)

        self.Init()
        self.Form.show()
        self.tRefresh()

    def Init(self):
        self.A_Save.clicked.connect(self.fA_Save)
        self.A_IPConnect.clicked.connect(self.fA_IPConnect)

        self.Config = configparser.ConfigParser()
        self.Config.read("./ScrcpyGUI.ini", encoding="utf-8-sig")
        self.ScrcpyPath = self.Config.get("Settings", "ScrcpyPath")
        self.CommandLine = self.Config.get("Settings", "CommandLine")
        self.A_Path.setText(self.ScrcpyPath)
        self.A_CommandLine.setText(self.CommandLine)

    def fA_Save(self):
        self.ScrcpyPath = self.A_Path.text().replace("%", "%%")
        self.CommandLine = self.A_CommandLine.text()
        
        self.Config.set("Settings", "ScrcpyPath", self.ScrcpyPath)
        self.Config.set("Settings", "CommandLine", self.CommandLine)

        with open("./ScrcpyGUI.ini", "w", encoding="utf-8-sig") as hConfig:
            self.Config.write(hConfig)

    def fA_IPConnect(self):
        IP = self.A_IPAddr.text()
        os.popen(os.path.join(self.ScrcpyPath + "adb.exe") + " connect " + IP).read()

    def Connect(self, name):
        os.popen(os.path.join(self.ScrcpyPath + "scrcpy.exe") + " -s " + name + " " + self.CommandLine).read()

    def Delete(self, name):
        os.popen(os.path.join(self.ScrcpyPath + "adb.exe") + " disconnect " + name).read()

    def tRefresh(self):
        start = time.time()
        while Flag:
            QtWidgets.QApplication.processEvents()
            end = time.time()
            if end - start >= 2:
                for index in range(self.A_Devices.rowCount()):
                    self.A_Devices.removeRow(0)
                popen = os.popen(os.path.join(self.ScrcpyPath + "adb.exe") + " devices")
                devices = popen.readlines()
                i = 0
                for line in devices:
                    if line == "List of devices attached\n":
                        break
                    i += 1
                devices = devices[i+1:-1]
                out = []
                for line in devices:
                    out.append(line.strip("\n").split("\t"))

                i = 0
                for Name, State in out:
                    self.A_Devices.insertRow(i)

                    r1 = QtWidgets.QWidget()
                    name = QtWidgets.QLabel(Name)
                    Layout = QtWidgets.QHBoxLayout()
                    Layout.addWidget(name)
                    Layout.setContentsMargins(5, 2, 5, 2)
                    r1.setLayout(Layout)
                    self.A_Devices.setCellWidget(i, 0, r1)

                    r2 = QtWidgets.QWidget()
                    state = QtWidgets.QLabel(State)
                    Layout = QtWidgets.QHBoxLayout()
                    Layout.addWidget(state)
                    Layout.setContentsMargins(5, 2, 5, 2)
                    r2.setLayout(Layout)
                    self.A_Devices.setCellWidget(i, 1, r2)

                    r3 = QtWidgets.QWidget()
                    Connect = QtWidgets.QPushButton('控制')
                    Connect.clicked.connect(partial(self.Connect, Name))
                    Delete = QtWidgets.QPushButton('断开')
                    Delete.clicked.connect(partial(self.Delete, Name))
                    Layout = QtWidgets.QHBoxLayout()
                    Layout.addWidget(Connect)
                    Layout.addWidget(Delete)
                    Layout.setContentsMargins(5, 2, 5, 2)
                    r3.setLayout(Layout)
                    self.A_Devices.setCellWidget(i, 2, r3)
                    i += 1
                start = time.time()

QApp = QtWidgets.QApplication([])

app = App()

state = QApp.exec_()
app.flag = False
sys.exit(state)