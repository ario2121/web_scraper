from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "boz"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 320
        self.UiComponents()
        self.InitWindow()
        

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon('home-icon.png'))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.show()

    def UiComponents(self):
        button = QPushButton("Click me",self)
        button.setGeometry(QRect(100,100,101,50))
        button.setIcon(QtGui.QIcon('home-icon.png'))
        button.setIconSize(QtCore.QSize(20,20))
        button.setToolTip("This Is Click Me Button")
        button.clicked.connect(self.ClickMe)
        exit_button = QPushButton("EXIT",self)
        exit_button.setGeometry(QRect(250,250,101,50))
        exit_button.clicked.connect(self.exit_app)


    def ClickMe(self):
        print('Hello Boz')

    def exit_app(self):
        sys.exit()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())