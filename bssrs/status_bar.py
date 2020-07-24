from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget,QStatusBar
import sys

from datetime import datetime


class StatusBar(QWidget):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.setMinimumSize(400, 400)

    def status_bar(self):
        bar = self.statusBar()
        bar.showMessage('Welcome to the Application', 5000)
        now = datetime.now()
        stime = QLabel(str(datetime.strftime(now, "%d-%m-%Y  %H:%M:%S")))
        sonline = QLabel("🙂")
        bar.addPermanentWidget(stime)
        bar.addPermanentWidget(sonline)

    def show_status_message(self, message, timeout):
        status = self.statusBar()
        if status.isVisible():
            status.showMessage(message, timeout)