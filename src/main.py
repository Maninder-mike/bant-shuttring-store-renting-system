from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QStyleFactory, QHBoxLayout, QDockWidget, QWidget, \
    QListWidget, QVBoxLayout, QAction, QMenu, QPushButton
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys

from src.status_bar import status_bar
from src.layout import gui_layout, layout_gui
from src.menubar import MenuBar
from src.toolbar import ToolBar


class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Bant Shuttering Store Renting System')
        self.setMinimumSize(1350, 700)

        gui_layout(self)
        status_bar(self)
        MenuBar.menu_bar_nono(self)
        ToolBar.tool_bar(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    win = MainWindow()
    sys.exit(app.exec_())
