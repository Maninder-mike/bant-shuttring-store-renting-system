from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QMenuBar, QMenu, QAction
import sys
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu('file')
        file.addAction('New')

        save = QAction('Save', self)
        save.setShortcut('Ctrl+S')
        file.addAction(save)

        edit = file.addMenu('Edit')
        edit.addAction('Copy')
        edit.addAction('Paste')
        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
