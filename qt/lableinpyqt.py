from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog, QVBoxLayout
import sys 
from PyQt5 import QtGui

class Window (QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 400
        self.iconName = "java.jpg"
        self.InitWindow()  

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()
        lable = QLabel("This is PyQt5 lable")
        vbox.addWidget(lable)

        lable2 = QLabel("this is seconde lable")
        lable2.setFont(QtGui.QFont('Sanserif',20))
        vbox.addWidget(lable2)

        self.setLayout(vbox)

        self.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
