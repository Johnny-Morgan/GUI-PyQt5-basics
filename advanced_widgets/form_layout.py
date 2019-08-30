import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Layout")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        form_layout = QFormLayout()
        #form_layout.setRowWrapPolicy(QFormLayout.WrapAllRows)

        name_txt = QLabel("Name: ")
        name_input = QLineEdit()

        password_text = QLabel("Password: ")
        password_input = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))

        form_layout.addRow(name_txt, name_input)
        form_layout.addRow(password_text, password_input)
        form_layout.addRow(QLabel("Country: "), QComboBox())
        form_layout.addRow(hbox)

        self.setLayout(form_layout)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()