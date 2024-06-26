# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Sabuhi\Documents\Python\Secure-RDC\ui_files\connect.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(350, 160)
        Main_Window.setMaximumSize(QtCore.QSize(350, 160))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_Window.setWindowIcon(icon)
        Main_Window.setAutoFillBackground(False)
        Main_Window.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_connect = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.btn_connect.setFont(font)
        self.btn_connect.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_connect.setMouseTracking(False)
        self.btn_connect.setTabletTracking(False)
        self.btn_connect.setAutoFillBackground(False)
        self.btn_connect.setStyleSheet("color:\'#0005ff\'\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/connect.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_connect.setIcon(icon1)
        self.btn_connect.setIconSize(QtCore.QSize(19, 19))
        self.btn_connect.setObjectName("btn_connect")
        self.gridLayout.addWidget(self.btn_connect, 5, 2, 1, 1)
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_password.setFont(font)
        self.input_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_password.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_password.setInputMask("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.input_password.setDragEnabled(True)
        self.input_password.setClearButtonEnabled(True)
        self.input_password.setObjectName("input_password")
        self.gridLayout.addWidget(self.input_password, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.input_ip_address = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip_address.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.input_ip_address.setFont(font)
        self.input_ip_address.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.input_ip_address.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.input_ip_address.setInputMask("")
        self.input_ip_address.setText("")
        self.input_ip_address.setDragEnabled(True)
        self.input_ip_address.setClearButtonEnabled(True)
        self.input_ip_address.setObjectName("input_ip_address")
        self.gridLayout.addWidget(self.input_ip_address, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "Secure RDC"))
        self.btn_connect.setText(_translate("Main_Window", "Connect"))
        self.btn_connect.setShortcut(_translate("Main_Window", "Enter"))
        self.input_password.setToolTip(_translate("Main_Window", "enter password"))
        self.input_password.setPlaceholderText(_translate("Main_Window", "password..."))
        self.input_ip_address.setToolTip(_translate("Main_Window", "enter IP address"))
        self.input_ip_address.setPlaceholderText(_translate("Main_Window", "IP address..."))
