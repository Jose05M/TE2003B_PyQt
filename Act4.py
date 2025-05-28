#pyuic5.exe -x p1.ui -o p1.py
import os
from PyQt5 import QtGui, QtCore
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from ui4 import *

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
        def __init__(self, *args, **kwargs):
                QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
                self.setupUi(self)

                name = self.int1.text()
                text = self.int2.text()
                num = self.int3.text()
                #-------------------------
                self.pushButton.clicked.connect(self.onClicked)

        def num_vocales(self):
                name = self.int1.text()
                name = name + ".txt"
                vocales = "aeiou"
                num_vocales = 0
                count = 0
                f = open(name, "r")
                lines = (f.readlines())
                for line in lines:
                        line = line.lower()
                        for i in line:
                                if i in vocales:
                                        count +=1
                f.close()
                self.out1.setText(f"{count}")

        def num_consonantes(self):
                name = self.int1.text()
                name = name + ".txt"
                consonantes = "bcdfghjklmnñpqrstvwxyz"
                num_consonantes = 0
                count = 0
                f = open(name, "r")
                lines = (f.readlines())
                for line in lines:
                        line = line.lower()
                        for i in line:
                                if i in consonantes:
                                        count +=1
                f.close()
                self.out2.setText(f"{count}")

        def onClicked(self):
                name = self.int1.text()
                text = self.int2.text()
                num = self.int3.text()
                num = int(num)
                name = name + ".txt"
                f = open(name, "w")
                for i in range (num):
                        f.write(f"{text}\n")
                f.close()
                self.num_vocales()
                self.num_consonantes()

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
