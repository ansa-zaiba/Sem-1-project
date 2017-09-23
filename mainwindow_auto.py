# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Nov 23 22:53:52 2016
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
        self.btnOff.setGeometry(QtCore.QRect(300, 40, 121, 101))
        self.btnOff.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(51, 189, 33, 78);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.btnOff.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/pi/SampleProgram/poweric.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btnOff.setIcon(icon1)
        self.btnOff.setIconSize(QtCore.QSize(100, 100))
        self.btnOff.setObjectName("btnOff")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnStat = QtWidgets.QPushButton(self.centralWidget)
        self.btnStat.setGeometry(QtCore.QRect(170, 140, 121, 111))
        self.btnStat.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(51, 189, 33, 78);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.btnStat.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/pi/SampleProgram/statusic.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btnStat.setIcon(icon2)
        self.btnStat.setIconSize(QtCore.QSize(100, 100))
        self.btnStat.setObjectName("btnStat")
        self.time = QtWidgets.QLCDNumber(self.centralWidget)
        self.time.setGeometry(QtCore.QRect(380, 220, 91, 31))
        self.time.setObjectName("time")
        self.btnOn = QtWidgets.QPushButton(self.centralWidget)
        self.btnOn.setGeometry(QtCore.QRect(50, 40, 111, 101))
        self.btnOn.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"selection-color: rgba(51, 189, 33, 78);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.btnOn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/pi/SampleProgram/startic.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btnOn.setIcon(icon3)
        self.btnOn.setIconSize(QtCore.QSize(80, 80))
        self.btnOn.setObjectName("btnOn")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Welcome To Biogas Control"))

