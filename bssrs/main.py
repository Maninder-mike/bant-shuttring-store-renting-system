import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow, QMessageBox, QToolBar, QCompleter, QLineEdit
from PyQt5.QtWidgets import QStyleFactory, QShortcut

from bssrs import __version__
from bssrs.config.base import get_image_path
from bssrs.config.dialogs import Dialogs, CustomerDatabase, SettingWindow
from bssrs.layout import gui_layout
from bssrs.status_bar import StatusBar


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

        self.show()

        self.menu_bar()
        self.tool_bar()

    def settings_window(self):
        dwin = SettingWindow()
        dwin.exec_()

    def dialog_window(self):
        dwin = CustomerDatabase()
        dwin.exec_()

    def menu_bar(self):
        file_menu = self.menuBar().addMenu("&File")
        edit_menu = self.menuBar().addMenu("&Edit")
        view_menu = self.menuBar().addMenu("&View")
        tools_menu = self.menuBar().addMenu("&Tools")
        help_menu = self.menuBar().addMenu("&Help")

        # ======== File ============
        file = QAction("File", self)
        file_menu.addAction(file)

        _open = QAction("Open", self)
        file_menu.addAction(_open)

        save = QAction(QIcon("images/add.png"), "Save", self)
        file_menu.addAction(save)
        file_menu.addSeparator()

        _exit = QAction(QIcon("images/exit.png"), "Exit", self)
        _exit.triggered.connect(self.close)
        file_menu.addAction(_exit)

        # ======== Edit ============
        preferences = QAction(QIcon("images/setting.png"), "Preferences", self)
        preferences.triggered.connect(self.settings_window)
        edit_menu.addAction(preferences)

        # ======== View ============
        plot = QAction(QIcon("images/pie.png"), "Plot", self)
        view_menu.addAction(plot)

        schema = QAction(QIcon("images/database.png"), "DB Schema", self)
        view_menu.addAction(schema)

        tincome = QAction(QIcon("images/notes.png"), "Today's Income", self)
        view_menu.addAction(tincome)

        view_menu.addSeparator()

        dockbar = QAction(QIcon("images/folder.png"), "Show Dockbar", self)
        view_menu.addAction(dockbar)

        cwindow = QAction(QIcon("images/user.png"), "Show Contacts Window", self)
        view_menu.addAction(cwindow)

        gwindow = QAction(QIcon("images/graph.png"), "Show Graph Window", self)
        view_menu.addAction(gwindow)

        view_menu.addSeparator()

        rdefault = QAction(QIcon("images/setting.png"), "Restore Default", self)
        view_menu.addAction(rdefault)

        # ======== Tools ============
        themes = QAction(QIcon("images/theme.ico"), "Themes", self)
        tools_menu.addAction(themes)

        # ======== Help ============
        feedback = QAction(QIcon("images/feedback.png"), "Feedback", self)
        help_menu.addAction(feedback)

        check_update = QAction(QIcon("images/update.png"), "Check Update", self)
        help_menu.addAction(check_update)

        help_menu.addSeparator()

        version = QAction(QIcon("images/version.ico"), "Version", self)
        version.triggered.connect(Dialogs.version_info)
        help_menu.addAction(version)

    def tool_bar(self):
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setIconSize(QSize(30, 30))
        self.addToolBar(toolbar)

        btn_add = QAction(QIcon("images/add.png"), "Add Customer", self)
        btn_add.triggered.connect(self.dialog_window)
        btn_add.setStatusTip("Add Customer")
        toolbar.addAction(btn_add)

        btn_edit = QAction(QIcon("images/edit.png"), "Edit Customer", self)
        btn_edit.triggered.connect(Dialogs.mainitemsdb)
        btn_edit.setStatusTip("Edit Customer")
        toolbar.addAction(btn_edit)

        btn_search = QAction(QIcon("images/Search.png"), "Search Customer", self)
        btn_search.setStatusTip("Search Customer")
        toolbar.addAction(btn_search)

        btn_delete = QAction(QIcon("images/garbage.png"), "Delete Customer", self)
        btn_delete.setStatusTip("Delete Customer")
        toolbar.addAction(btn_delete)

        toolbar.addSeparator()

        sample = ["Apple", "Alps", "Berry", "Cherry"]
        completer = QCompleter(sample)
        search = QLineEdit()
        search.setPlaceholderText(" Search here all items.")
        search.setMaximumSize(QSize(300, 30))
        search.setCompleter(completer)
        search.setToolTip("Search all data, names, dates, and bills")
        toolbar.addWidget(search)

        btn_search = QAction(QIcon("images/search1.ico"), "Search", self)
        btn_search.setStatusTip("Search")
        toolbar.addAction(btn_search)

    def version(self):
        return QMessageBox.information(self, 'Programme version', __version__)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('windowsvista'))
    win = MainWindow()
    sys.exit(app.exec_())
