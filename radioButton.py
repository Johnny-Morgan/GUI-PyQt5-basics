import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("checkbox test")
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.name.move(150, 50)
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")
        self.surname.move(150, 80)
        self.male = QRadioButton("Male", self)
        self.male.setChecked(True)
        self.male.move(150, 110)
        self.female = QRadioButton("Female", self)
        self.female.move(200, 110)
        button = QPushButton("Submit", self)
        button.move(150, 140)
        button.clicked.connect(self.getValues)

        self.show()

    def getValues(self):
        if self.male.isChecked():
            print("Name : " + self.name.text() + "\nSurname : " + self.surname.text() + "\nYou are male")
        else:
            print("Name : " + self.name.text() + "\nSurname : " + self.surname.text() + "\nYou are female")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()