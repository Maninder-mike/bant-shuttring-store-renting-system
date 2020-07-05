from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

from datetime import datetime


class StatusBar(QMainWindow):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.setMinimumSize(400, 400)

        self.status_bar()
        self.show()

    def status_bar(self):
        bar = self.statusBar()
        bar.showMessage('Welcome to the Application', 5000)

        now = datetime.now()
        self.stime = QLabel(str(datetime.strftime(now, "%d-%m-%Y,  %H:%M:%S")))
        self.sonline = QLabel("🙂")

        bar.addPermanentWidget(self.stime)
        bar.addPermanentWidget(self.sonline)

    def show_status_message(self, message, timeout):
        status = self.statusBar()
        if status.isVisible():
            status.showMessage(message, timeout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StatusBar()
    sys.exit(app.exec_())
