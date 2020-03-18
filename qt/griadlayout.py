from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Griad Layout"
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

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox('What IS Your Favorite Programing Language?')
        gridLayout = QGridLayout()

        button = QPushButton("Python",self)
        button.setIcon(QtGui.QIcon('download.jpeg'))
        button.setIconSize(QtCore.QSize(40,40))
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0, 0)

        button1 = QPushButton("Java",self)
        button1.setIcon(QtGui.QIcon('java.jpg'))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button1, 0, 1)

        button3 = QPushButton("C++",self)
        button3.setIcon(QtGui.QIcon('c++.jpeg'))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button3, 1, 0)

        button2 = QPushButton("C#",self)
        button2.setIcon(QtGui.QIcon('c#.png'))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button2, 1, 1)

        self.groupBox.setLayout(gridLayout)
    

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())