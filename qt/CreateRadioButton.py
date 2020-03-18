from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow,QVBoxLayout,QGroupBox,QHBoxLayout,QPushButton,QRadioButton,QDialog
import sys
from PyQt5 import QtGui  
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "RadioButton"
        self.top = 300
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = 'c#.png'


        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.lable = QLabel(self)
        self.lable.setFont(QtGui.QFont("Sanserif",20))
        vbox.addWidget(self.lable)

        self.setLayout(vbox)

        self.show()


    def radioButton(self):
        self.groupBox = QGroupBox("What Is Favorite Programing Langage?")
        self.groupBox.setFont(QtGui.QFont("Sanserif",14))

        hboxLayout = QHBoxLayout()

        self.radiobtn1 = QRadioButton("Python")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setIcon(QtGui.QIcon('download.jpeg'))
        self.radiobtn1.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Java")
        self.radiobtn2.setIconSize(QtCore.QSize(40,40))
        self.radiobtn2.setIcon(QtGui.QIcon('java.jpg'))
        self.radiobtn2.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("C++")
        self.radiobtn3.setIconSize(QtCore.QSize(40,40))
        self.radiobtn3.setIcon(QtGui.QIcon('c++.jpeg'))
        self.radiobtn3.toggled.connect(self.onRadioButton)
        hboxLayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxLayout)

    def onRadioButton(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.lable.setText("you have selected "+ radioBtn.text())






if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())