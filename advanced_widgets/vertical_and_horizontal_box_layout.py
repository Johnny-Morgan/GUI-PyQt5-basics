import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical and Horizontal Box Layout")
        self.setGeometry(50, 50, 400, 400)
        self.UI()

    def UI(self):
        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        button1 = QPushButton()
        button2 = QPushButton()

        top_layout.setContentsMargins(100, 10, 20, 20) #left, top, right, bottom
        top_layout.addWidget(cbox)
        top_layout.addWidget(rbtn)
        top_layout.addWidget(combo)

        bottom_layout.setContentsMargins(150, 10, 150, 10)
        bottom_layout.addWidget(button1)
        bottom_layout.addWidget(button2)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)




        self.setLayout(main_layout)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()