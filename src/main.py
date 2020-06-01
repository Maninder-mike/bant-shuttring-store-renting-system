from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QStyleFactory, QHBoxLayout, QDockWidget, QWidget, \
    QListWidget, QVBoxLayout, QAction
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
import sys

from src.tab_widget import TabWidget
from src.toolbox import ToolBox
from src.status_bar import StatusBar
from src.layout import Layout


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
        self.setMinimumSize(1000, 600)

        self.status_bar()
        self.gui_layout()
        self.menu_bar()
        self.tool_bar()
        self.show()

    def gui_layout(self):
        main_layout = QHBoxLayout()
        layout1 = QVBoxLayout()
        right_layout = QHBoxLayout()

        toolbox = ToolBox()

        layout1.addWidget(toolbox)
        layout1.addWidget(Color('pink'))
        layout1.addWidget(Color('blue'))

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addLayout(layout1)
        table = TabWidget()
        main_layout.addWidget(table)

        right_layout.addWidget(self.right_up_text_edit())
        right_layout.addWidget(self.right_down_text_edit())

        main_layout.addLayout(right_layout)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def right_up_text_edit(self):
        layout = QHBoxLayout()

        items = QDockWidget("Contacts", self)

        listWidget = QListWidget()
        listWidget.addItem('Item1')
        items.setWidget(listWidget)
        items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, items)
        self.setLayout(layout)

    def right_down_text_edit(self):
        layout = QHBoxLayout()

        items = QDockWidget("Payable", self)

        listWidget = QListWidget()
        listWidget.addItem('Item1')
        items.setWidget(listWidget)
        items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, items)
        self.setLayout(layout)

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
