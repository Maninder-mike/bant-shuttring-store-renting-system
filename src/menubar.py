from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QMenu, QMenuBar
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

        self.file_menu()
        self.edit_menu()
        self.tool_menu()
        self.window_menu()
        self.help_menu()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
