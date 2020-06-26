import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from bssrs.config.dialogs import version_info
from bssrs.config.preferences import TabWidget


class MenuBar(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)

        self.menubar_one()
        self.show()

    def menubar_one(self):

        self.file_menu()
        self.edit_menu()
        self.view_menu()
        self.tool_menu()
        self.help_menu()
        self.menu_bar()

    def file_menu(self):
        pass

    def edit_menu(self):
        pass

    def view_menu(self):
        pass

    def tool_menu(self):
        pass

    def help_menu(self):
        pass

    def toggle_menu(self, state):
        if state:
            self.status_bar().show()
        else:
            self.status_bar().hide()

    def menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction('Open')
        file_menu.addAction('Save')
        file_menu.addSeparator()
        file_menu.addAction('Exit', self.close)

        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Preferences', TabWidget)

        view_menu = menu_bar.addMenu('View')
        view_menu.addAction('Plot')
        view_menu.addAction('DB Schema')
        view_menu.addAction("Today's Income")
        view_menu.addSeparator()
        view_menu.addAction('Show Dockbar')
        view_menu.addAction('Show Contacts Window')
        view_menu.addAction('Show Graph Window')
        view_menu.addSeparator()
        view_menu.addAction('Restore Default')

        tools_menu = menu_bar.addMenu('Tools')
        tools_menu.addAction('Themes')

        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction('Feedback')
        help_menu.addAction('Check Update')
        help_menu.addSeparator()
        help_menu.addAction('Version', version_info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MenuBar()
    sys.exit(app.exec_())
