import sys

from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QShortcut

from bssrs.config.base import get_image_path
from bssrs.layout import gui_layout
from bssrs.menubar import MenuBar
from bssrs.status_bar import StatusBar
from bssrs.toolbar import tool_bar


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Bant Shuttering Store Renting System')

        self.setMinimumSize(1350, 700)

        app_icon = QIcon(get_image_path("root_icon.ico"))
        self.setWindowIcon(app_icon)

        self.shortcut_close = QShortcut(QKeySequence('Ctrl+Q'), self)
        self.shortcut_close.activated.connect(lambda: app.quit())

        gui_layout(self)
        StatusBar.status_bar(self)
        MenuBar.menu_bar(self)
        tool_bar(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('windowsvista'))
    win = MainWindow()
    sys.exit(app.exec_())
