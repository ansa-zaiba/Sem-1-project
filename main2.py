#!/usr/bin/python

# This gets the Qt stuff
from PyQt5 import QtGui, QtCore, QtWidgets

# always seem to need this
import sys
import os
from time import strftime
import sqlite3
from threading import Thread
# This is our window from QtCreator
import ui_mainwindow2

# create class for our Raspberry Pi GUI
class MainWindow(QtWidgets.QMainWindow, ui_mainwindow2.Ui_MainWindow):
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
        
        self.temp_reader=Thread(target=self.readTemp)
        self.temp_reader.start()
        
        ### Hooks to for buttons
        #self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        self.btnOff.clicked.connect(lambda: self.pressedOffButton())
        self.btnStat.clicked.connect(lambda: self.pressedStatButton())
        #self.time.display(strftime("%H"+":"+"%M"))
        
    def readTemp(self):
        db=sqlite3.connect('/home/pi/SampleProgram/data.db')
        while True:
            try:
                min_row=db.execute('select min(oid) from temperature').fetchone()[0]
                max_row=db.execute('select max(oid) from temperature').fetchone()[0]
                if (max_row-min_row)>3600:
                    db.execute('delete from temperature where oid<max_row')
                current_temp=db.execute('select temperature from temperature where oid=(?)',[max_row]).fetchone()[0]
                self.temp.display(current_temp)
                db.commit()
            except:
                continue
            


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
