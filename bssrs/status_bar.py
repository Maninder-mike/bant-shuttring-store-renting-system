from PyQt5.QtWidgets import QStatusBar, QWidget, QApplication, QMainWindow
import sys


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()

        self.status_bar()
        self.show()

    def status_bar(self):
        self.bar = QStatusBar()
        self.bar.showMessage('Welcome to the Application', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StatusBar()
    sys.exit(app.exec_())


def status_bar(self):
    bar = self.statusBar()
    bar.showMessage('Welcome to the Application', 5000)
