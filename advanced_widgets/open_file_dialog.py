import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Dialogs")
        self.setGeometry(350, 150, 400, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        file_button = QPushButton("Open File")
        file_button.clicked.connect(self.open_file)
        font_button = QPushButton("Change Font")
        font_button.clicked.connect(self.change_font)
        colour_button = QPushButton("Change Colour")
        colour_button.clicked.connect(self.change_colour)
        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addStretch()
        hbox.addWidget(file_button)
        hbox.addWidget(font_button)
        hbox.addWidget(colour_button)
        hbox.addStretch()
        self.setLayout(vbox)
        self.show()

    def open_file(self):
        url = QFileDialog.getOpenFileName(self, "Open a file", "", "All Files(*);;*txt")
        print(url[0])
        file = open(url[0], 'r')
        content = file.read()
        self.editor.setText(content)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.editor.setCurrentFont(font)

    def change_colour(self):
        colour= QColorDialog.getColor()
        self.editor.setTextColor(colour)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()