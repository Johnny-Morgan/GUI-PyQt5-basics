import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget")
        self.setGeometry(350, 150, 600, 600)
        self.UI()

    def UI(self):
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "First Tab")
        self.tabs.addTab(self.tab2, "Second Tab")
        self.tabs.addTab(self.tab3, "Third Tab")

        #####Widgets####
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.text = QLabel("Hello")
        self.btn1 = QPushButton("1st Tab")
        self.btn1.clicked.connect(self.btn_func)
        self.btn2 = QPushButton("2nd Tab")
        vbox.addWidget(self.text)
        vbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        self.tab1.setLayout(vbox)
        self.tab2.setLayout(hbox)
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.show()

    def btn_func(self):
        self.text.setText("Button is active")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()