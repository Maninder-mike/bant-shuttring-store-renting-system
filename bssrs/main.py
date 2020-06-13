import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory
from PyQt5.QtGui import QIcon
from bssrs.status_bar import status_bar
from bssrs.layout import gui_layout
from bssrs.menubar import MenuBar
from bssrs.toolbar import ToolBar
from qtpy import PYQT5
from bssrs.config.base import get_image_path


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Bant Shuttering Store Renting System')
        self.setMinimumSize(1350, 700)

        if PYQT5:
            app_icon = QIcon(get_image_path("root_icon.ico"))
        else:
            app_icon = QIcon(get_image_path("root_icon.ico"))
        self.setWindowIcon(app_icon)

        gui_layout(self)
        status_bar(self)
        MenuBar.menu_bar(self)
        ToolBar.tool_bar(self)
        self.show()

    def show_status_message(self, message, timeout):
        """
        Show a status message in bssrs Main Window.
        """
        status = self.statusBar()
        if status.isVisible():
            status.showMessage(message, timeout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('windowsvista'))
    win = MainWindow()
    sys.exit(app.exec_())
