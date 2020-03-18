from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QDialog,QVBoxLayout
import sys
from PyQt5 import QtGui  
from PyQt5.QtGui import QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "boz"
        self.top = 500
        self.left = 200
        self.width = 500
        self.height = 400
        self.iconName = 'c#.png'


        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        lableImaige = QLabel(self)

        pixmap = QPixmap("download.jpeg")

        lableImaige.setPixmap(pixmap)

        vbox.addWidget(lableImaige)

        self.setLayout(vbox)
        
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

