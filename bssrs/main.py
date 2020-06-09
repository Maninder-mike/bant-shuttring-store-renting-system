import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
from bssrs.status_bar import status_bar
from bssrs.layout import gui_layout
from bssrs.menubar import MenuBar
from bssrs.toolbar import ToolBar


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Bant Shuttering Store Renting System')
        self.setMinimumSize(1350, 700)

        gui_layout(self)
        status_bar(self)
        MenuBar.menu_bar(self)
        ToolBar.tool_bar(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('windowsvista'))
    win = MainWindow()
    sys.exit(app.exec_())
