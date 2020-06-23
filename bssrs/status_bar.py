from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.setMinimumSize(400, 400)

        self.status_bar()
        self.show()

    def status_bar(self):
        bar = self.statusBar()
        bar.showMessage('Welcome to the Application', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StatusBar()
    sys.exit(app.exec_())
