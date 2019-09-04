import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

count = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar widget")
        self.setGeometry(350, 150, 500, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.progress_bar = QProgressBar()
        btn_start = QPushButton("Start")
        btn_start.clicked.connect(self.timer_start)
        btn_stop = QPushButton("Stop")
        btn_stop.clicked.connect(self.timer_stop)

        self.timer = QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.run_progress_bar)
        vbox.addWidget(self.progress_bar)
        vbox.addLayout(hbox)
        hbox.addWidget(btn_start)
        hbox.addWidget(btn_stop)

        self.setLayout(vbox)
        self.show()

    def run_progress_bar(self):
        global count
        count += 1
        print(count)
        self.progress_bar.setValue(count)
        if count == 100:
            self.timer.stop()

    def timer_start(self):
        self.timer.start()

    def timer_stop(self):
        self.timer.stop()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()