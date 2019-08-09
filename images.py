import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

# program that displays an image and has 2 buttons that remove and show the image

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("Image")
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("images/python.jpg"))
        self.image.move(140, 50)
        removeButton = QPushButton("Remove", self)
        removeButton.move(160, 350)
        removeButton.clicked.connect(self.removeImg)
        showButton = QPushButton("Show", self)
        showButton.move(270, 350)
        showButton.clicked.connect(self.showImg)

        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()