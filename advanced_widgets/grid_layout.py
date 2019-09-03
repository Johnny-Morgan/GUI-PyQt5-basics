import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        self.grid_layout = QGridLayout()
        # button1 = QPushButton("Button1")
        # button2 = QPushButton("Button2")
        # button3 = QPushButton("Button3")
        # button4 = QPushButton("Button4")
        # self.grid_layout.addWidget(button1, 0, 0)
        # self.grid_layout.addWidget(button2, 0, 1)
        # self.grid_layout.addWidget(button3, 1, 0)
        # self.grid_layout.addWidget(button4, 1, 1)

        for i in range(0, 4):
            for j in range(0, 4):
                button = QPushButton("Button{}{}".format(i, j))
                self.grid_layout.addWidget(button, i, j)

        self.setLayout(self.grid_layout)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()