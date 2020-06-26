from PyQt5.QtWidgets import QDialog, QPushButton,QLabel
from PyQt5.Qt import Qt

from bssrs import __version__

def show_dialog(self):
    d = QDialog()
    b1 = QPushButton("ok", d)
    b1.move(50, 50)
    d.setFixedSize(200, 200)
    d.setWindowTitle("Button Edit Window")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()


def version_info():
    d = QDialog()
    b1 = QPushButton(str(__version__), d)
    b1.move(50, 50)
    d.setFixedSize(200, 200)
    d.setWindowTitle("Button Edit Window")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()