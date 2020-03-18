from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layout Management"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.iconName = 'home-icon.png'

        self.InitWindow()
        


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Sport ?")

        hboxlayout = QHBoxLayout()

        button = QPushButton("Football",self)
        button.setIcon(QtGui.QIcon('home-icon.png'))
        button.setIconSize(QtCore.QSize(40,40))
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        
        button2 = QPushButton("PUBG",self)
        button2.setIcon(QtGui.QIcon('home-icon.png'))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        
        button1 = QPushButton("SEX",self)
        button1.setIcon(QtGui.QIcon('home-icon.png'))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        hboxlayout.addWidget(button1)
        
        self.groupBox.setLayout(hboxlayout)
        

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
