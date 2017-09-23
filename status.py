#!/usr/bin/python

# This gets the Qt stuff
from PyQt5 import QtGui, QtCore, QtWidgets

# always seem to need this
import sys
import os

# This is our window from QtCreator
import status_auto

# create class for our Raspberry Pi GUI
class Status(QtWidgets.QMainWindow, status_auto.Ui_status):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedOkButton(self):
        sys.exit()
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.Ok.clicked.connect(lambda: self.pressedOkButton())
        
# I feel better having one of these
def main():
    # a new app instance
    app = QtWidgets.QApplication(sys.argv)
    form = Status()
    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(QtGui.QPixmap("/home/pi/SampleProgram/biogassymbol.jpg")))

    form.setPalette(palette)
    form.setWindowTitle("Status Window")                                                            
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()

