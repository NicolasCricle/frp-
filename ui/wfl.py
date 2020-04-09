# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wfl.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QSizePolicy, QWidget, QGridLayout, QTextEdit, QPushButton, QLabel, QLineEdit, QMenuBar, \
    QMenu, QStatusBar, QAction


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        # 窗口主题设置 尺寸以及固定
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(470, 500)
        mainWindow.setFixedSize(470, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)

        # 设置窗口文字字体
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setBold(False)
        font.setWeight(50)
        mainWindow.setFont(font)

        # 设置窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/wfl.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 180, 431, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # 状态输出控件
        self.outPrint = QTextEdit(self.centralwidget)
        self.outPrint.setGeometry(QtCore.QRect(20, 230, 431, 221))
        self.outPrint.setReadOnly(True)
        self.outPrint.setObjectName("outPrint")

        # frp开启按钮
        self.frpOn = QPushButton(self.layoutWidget)
        self.frpOn.setObjectName("frpOn")
        self.gridLayout_2.addWidget(self.frpOn, 0, 0, 1, 1)

        # frp关闭按钮
        self.frpOff = QPushButton(self.layoutWidget)
        self.frpOff.setObjectName("frpOff")
        self.gridLayout_2.addWidget(self.frpOff, 0, 1, 1, 1)

        # nginx开启按钮
        self.nginxOn = QPushButton(self.layoutWidget)
        self.nginxOn.setObjectName("nginxOn")
        self.gridLayout_2.addWidget(self.nginxOn, 0, 2, 1, 1)

        # nginx关闭按钮
        self.nginxOff = QPushButton(self.layoutWidget)
        self.nginxOff.setObjectName("nginxOff")
        self.gridLayout_2.addWidget(self.nginxOff, 0, 3, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 16, 431, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # frp文件
        self.frpName = QLabel(self.widget)
        self.frpName.setObjectName("frpName")
        self.gridLayout.addWidget(self.frpName, 0, 0, 1, 1)

        # frp文件输入框
        self.dirNameEdit = QLineEdit(self.widget)
        self.dirNameEdit.setEnabled(True)
        self.dirNameEdit.setText("")
        self.dirNameEdit.setDragEnabled(False)
        self.dirNameEdit.setReadOnly(False)
        self.dirNameEdit.setObjectName("dirNameEdit")
        self.gridLayout.addWidget(self.dirNameEdit, 0, 1, 1, 1)

        # frp路径自动搜索
        self.autoSearch = QPushButton(self.widget)
        self.autoSearch.setObjectName("autoSearch")
        self.gridLayout.addWidget(self.autoSearch, 0, 2, 1, 1)

        # serverIp
        self.serverIp = QLabel(self.widget)
        self.serverIp.setObjectName("serverIp")
        self.gridLayout.addWidget(self.serverIp, 1, 0, 1, 1)

        # serverIp 编辑
        self.serverIpEdit = QLineEdit(self.widget)
        self.serverIpEdit.setText("")
        self.serverIpEdit.setObjectName("serverIpEdit")
        self.gridLayout.addWidget(self.serverIpEdit, 1, 1, 1, 1)

        # serverUser
        self.serverUser = QLabel(self.widget)
        self.serverUser.setObjectName("serverUser")
        self.gridLayout.addWidget(self.serverUser, 2, 0, 1, 1)

        # serverUser 编辑
        self.serverUserEdit = QLineEdit(self.widget)
        self.serverUserEdit.setText("")
        self.serverUserEdit.setObjectName("serverUserEdit")
        self.gridLayout.addWidget(self.serverUserEdit, 2, 1, 1, 1)

        # serverPassword
        self.serverPassword = QLabel(self.widget)
        self.serverPassword.setObjectName("serverPassword")
        self.gridLayout.addWidget(self.serverPassword, 3, 0, 1, 1)


        # serverPassword 编辑
        self.serverPasswordEdit = QLineEdit(self.widget)
        self.serverPasswordEdit.setText("")
        self.serverPasswordEdit.setObjectName("serverPasswordEdit")
        self.gridLayout.addWidget(self.serverPasswordEdit, 3, 1, 1, 1)
        # 设置密码不可见不可复制
        self.serverPasswordEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.serverPasswordEdit.setEchoMode(QLineEdit.Password)

        # nginxStream
        self.nginxStream = QLabel(self.widget)
        self.nginxStream.setObjectName("nginxStream")
        self.gridLayout.addWidget(self.nginxStream, 4, 0, 1, 1)

        # nginxStream 编辑
        self.nginxStreamEdit = QLineEdit(self.widget)
        self.nginxStreamEdit.setText("")
        self.nginxStreamEdit.setObjectName("nginxStreamEdit")
        self.gridLayout.addWidget(self.nginxStreamEdit, 4, 1, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)

        # 菜单栏设置
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)

        # 状态栏设置
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)


        self.openConf = QAction(mainWindow)
        self.openConf.setObjectName("openConf")
        self.menu.addSeparator()
        self.menu.addAction(self.openConf)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.frpOn.clicked.connect(self.frp_on)
        self.frpOff.clicked.connect(self.frp_off)
        self.autoSearch.clicked.connect(self.auto_search)
        self.nginxOn.clicked.connect(self.nginx_on)
        self.nginxOff.clicked.connect(self.nginx_off)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "FRP管理"))
        self.frpOn.setText(_translate("mainWindow", "开启FRP"))
        self.frpOff.setText(_translate("mainWindow", "关闭FRP"))
        self.nginxOn.setText(_translate("mainWindow", "开启Nginx"))
        self.nginxOff.setText(_translate("mainWindow", "关闭Nginx"))
        self.frpName.setText(_translate("mainWindow", "frp文件夹"))
        self.autoSearch.setText(_translate("mainWindow", "自动搜索"))
        self.serverIp.setText(_translate("mainWindow", "服务器Ip"))
        self.serverUser.setText(_translate("mainWindow", "服务器用户名"))
        self.serverPassword.setText(_translate("mainWindow", "服务器密码"))
        self.nginxStream.setText(_translate("mainWindow", "stream名称"))
        self.menu.setTitle(_translate("mainWindow", "设置"))
        self.openConf.setText(_translate("mainWindow", "打开配置文件"))
