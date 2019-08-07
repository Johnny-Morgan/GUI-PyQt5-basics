import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 350, 350)
        self.setWindowTitle("Please login")
        self.UI()

    def UI(self):
        usernameLabel = QLabel("Username", self)
        usernameLabel.move(50, 50)

        self.usernameTextBox = QLineEdit(self)
        self.usernameTextBox.setPlaceholderText("Username")
        self.usernameTextBox.move(110, 50)

        passwordLabel = QLabel("Password", self)
        passwordLabel.move(50, 80)

        self.passwordTextBox = QLineEdit(self)
        self.passwordTextBox.setPlaceholderText("Password")
        self.passwordTextBox.setEchoMode(QLineEdit.Password)
        self.passwordTextBox.move(110, 80)

        loginButton = QPushButton("Login", self)
        loginButton.move(50, 110)
        loginButton.clicked.connect(self.getUsername)

        self.show()

    def getUsername(self):
        username = self.usernameTextBox.text()
        self.setWindowTitle("Welcome " + username)

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()