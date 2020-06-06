from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.menubar = MenuBar()
        self.setCentralWidget(self.menubar)

        self.show()


class MenuBar(QWidget):
    def __init__(self, *args, **kwargs):
        super(MenuBar, self).__init__(*args, **kwargs)

        self.menubar_one()

    def menubar_one(self):

        self.file_menu()
        self.edit_menu()
        self.tool_menu()
        self.window_menu()
        self.help_menu()
        self.menu_bar()

    def file_menu(self):
        pass

    def edit_menu(self):
        pass

    def tool_menu(self):
        pass

    def window_menu(self):
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
        edit_menu.addAction('Undo')

        window_menu = menu_bar.addMenu('Window')
        window_menu.addAction('Themes')

        help_menu = menu_bar.addMenu('Help')
        help_menu.addAction('Info')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())

# layout = QVBoxLayout()
#        bar = self.menuBar()
#        file = bar.addMenu('file')
#        file.addAction('New')
#
#        save = QAction('Save', self)
#        save.setShortcut('Ctrl+S')
#        file.addAction(save)
#
#        edit = file.addMenu('Edit')
#        edit.addAction('Copy')
#        edit.addAction('Paste')
#        self.setLayout(layout)
