from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.Qt import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(500, 500)

        self.bar = StatusBar()
        self.setCentralWidget(self.bar)

        self.show()


class StatusBar(QWidget):
    def __init__(self, *args, **kwargs):
        super(StatusBar, self).__init__(*args, **kwargs)
        self.status_bar()

    def status_bar(self):
        bar = self.statusBar()
        bar.showMessage('Welcome to the Application', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
