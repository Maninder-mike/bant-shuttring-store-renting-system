from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5.Qt import Qt


def show_dialog(self):
    d = QDialog()
    b1 = QPushButton("ok", d)
    b1.move(50, 50)
    d.setFixedSize(200, 200)
    d.setWindowTitle("Button Edit Window")
    d.setWindowModality(Qt.ApplicationModal)
    d.exec_()
