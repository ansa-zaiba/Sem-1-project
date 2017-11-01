# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created: Mon Oct 16 22:48:36 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        font = QtGui.QFont()
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("biogassymbol.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("biogassymbol.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("biogassymbol.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(24, 24))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnOff = QtWidgets.QPushButton(self.centralWidget)
        self.btnOff.setGeometry(QtCore.QRect(320, 190, 121, 101))
        self.btnOff.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(51, 189, 33, 78);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.btnOff.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("poweric.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btnOff.setIcon(icon1)
        self.btnOff.setIconSize(QtCore.QSize(100, 100))
        self.btnOff.setObjectName("btnOff")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(90, 0, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnStat = QtWidgets.QPushButton(self.centralWidget)
        self.btnStat.setGeometry(QtCore.QRect(40, 190, 121, 111))
        self.btnStat.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(51, 189, 33, 78);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.btnStat.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("statusic.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btnStat.setIcon(icon2)
        self.btnStat.setIconSize(QtCore.QSize(100, 100))
        self.btnStat.setObjectName("btnStat")
        self.temp = QtWidgets.QLCDNumber(self.centralWidget)
        self.temp.setGeometry(QtCore.QRect(190, 100, 91, 31))
        self.temp.setProperty("intValue", 0)
        self.temp.setObjectName("temp")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 101, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome To Biogas Control"))
        self.label_2.setText(_translate("MainWindow", "Temperature"))

