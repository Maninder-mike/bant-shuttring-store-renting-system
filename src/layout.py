from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout, QDockWidget, QListWidget, \
    QTextEdit
from src.toolbox import ToolBox
from src.tab_widget import TabWidget
from PyQt5.Qt import Qt, QSize


def layout_gui(self):
    main_layout = QHBoxLayout()
    layout1 = QVBoxLayout()
    right_layout = QHBoxLayout()

    toolbox = ToolBox()

    layout1.addWidget(toolbox)

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


def gui_layout(self):
    main_layout = QHBoxLayout()
    layout1 = QVBoxLayout()
    right_layout = QHBoxLayout()

    toolbox = ToolBox()
    toolbox.setToolTip("Find all items here.")

    layout1.addWidget(toolbox)
    layout1.setAlignment(Qt.AlignLeft)

    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)
    main_layout.addLayout(layout1)

    table = TabWidget()
    table.setMinimumWidth(800)
    main_layout.addWidget(table)

    right_layout.addWidget(right_up_text_edit(self))
    right_layout.addWidget(right_down_text_edit(self))

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

    lst = 'Bant Shuttering Store Renting System'.split(" ")

    list_widget = QListWidget()
    list_widget.addItems(lst)
    items.setWidget(list_widget)
    items.setFloating(False)
    self.setCentralWidget(QTextEdit())
    self.addDockWidget(Qt.RightDockWidgetArea, items)
    self.setLayout(layout)
