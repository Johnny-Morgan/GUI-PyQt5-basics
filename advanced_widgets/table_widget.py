import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Table Widget")
        self.setGeometry(350, 150, 600, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.table = QTableWidget()
        btn = QPushButton("Get data")

        self.table.setRowCount(5)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("First Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Surname"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("Email"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Phone"))
        #self.table.verticalHeader().hide()
        self.table.setItem(0, 0, QTableWidgetItem("John"))
        self.table.setItem(0, 1, QTableWidgetItem("Morgan"))
        self.table.setItem(0, 2, QTableWidgetItem("jwjmorgan@gmail.com"))
        self.table.setItem(0, 3, QTableWidgetItem("086 060 4249"))
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # cells cannot be edited by user
        self.table.doubleClicked.connect(self.double_clicked)
        btn.clicked.connect(self.get_value)
        vbox.addWidget(self.table)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        self.show()

    def get_value(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

    def double_clicked(self):
        for item in self.table.selectedItems():
            print(item.text(), item.row(), item.column())

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()