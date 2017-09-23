#!/usr/bin/python

# This gets the Qt stuff
from PyQt5 import QtGui, QtCore, QtWidgets

# always seem to need this
import sys
import os
from time import strftime

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QtWidgets.QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedOnButton(self):
        os.system('python /home/pi/SampleProgram/sensor.py')

    def pressedOffButton(self):

        os.system('sudo shutdown now -h')

    def pressedStatButton(self):
        os.system('python /home/pi/SampleProgram/status.py')

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())
        self.btnStat.clicked.connect(lambda: self.pressedStatButton())
        self.time.display(strftime("%H"+":"+"%M"))


# I feel better having one of these
def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("/home/pi/SampleProgram/biogassymbol.jpg")))

    form.setPalette(palette)
    form.setWindowTitle("Main Window")
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
