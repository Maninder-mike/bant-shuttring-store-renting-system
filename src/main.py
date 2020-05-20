from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QMenu, QMenuBar, QGridLayout, QStyleFactory, \
    QPushButton, QHBoxLayout, QLineEdit, QDockWidget, QWidget, QListWidget, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Bant Shuttering Store Renting System')
        self.setMinimumSize(1000, 600)

        layout = QHBoxLayout()
        layout_2 = QVBoxLayout()

        self.line_edit = QLineEdit()
        # self.btn.resize(QSize(20, 50))
        self.text_edit = QTextEdit()
        # self.setCentralWidget(self.text_edit)

        self.items = QDockWidget("Datable", self)
        self.items_2 = QDockWidget("Bottom", self)

        self.listWidget = QListWidget()
        self.listWidget.addItem('Item1')
        self.listWidget.addItem('Item2')
        self.listWidget.addItem('Item3')
        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)

        self.menu_bar()
        self.tool_bar()
        self.status_bar()
        self.show()

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

    def tool_bar(self):
        edit_toolbar = self.addToolBar('Edit')
        edit_toolbar.addAction('Undo')
        edit_toolbar.addAction('Redo')
        edit_toolbar.addAction('Cut')
        edit_toolbar.addAction('Copy')
        edit_toolbar.addAction('Paste')

        view_toolbar = self.addToolBar('View')
        view_toolbar.addAction('Themes')
        view_toolbar.addAction('Recent Files')
        view_toolbar.addAction('Location')
        view_toolbar.addAction('Contact Info')

    def status_bar(self):
        bar = self.statusBar()
        bar.showMessage('Welcome to the Application', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    win = MainWindow()
    sys.exit(app.exec_())

# container = QWidget()
# container_layout = QVBoxLayout()
# container.setLayout(container_layout)
#
# self.setCentralWidget(container)
