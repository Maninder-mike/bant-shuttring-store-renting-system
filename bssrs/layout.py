from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QDockWidget, QListWidget

from bssrs.tab_widget import TabWidget, GraphWidget
from bssrs.toolbox import ToolBox


def right_up_text_edit(self):
    layout = QHBoxLayout()
    header = QDockWidget("Contacts", self)
    header.setFixedWidth(350)

    list_widget = QListWidget()
    list_widget.addItem('Item1')
    header.setWidget(list_widget)
    # self.setCentralWidget(QTextEdit())
    self.addDockWidget(Qt.RightDockWidgetArea, header)
    self.setLayout(layout)


def right_down_text_edit(self):
    layout = QHBoxLayout()

    items = QDockWidget("Graphs", self)
    items.setFixedWidth(350)
    items.setMinimumHeight(300)

    graph_tab = GraphWidget()

    items.setWidget(graph_tab)
    items.setFloating(False)
    # self.setCentralWidget(QTextEdit())
    self.addDockWidget(Qt.RightDockWidgetArea, items)
    self.setLayout(layout)


def gui_layout(self):
    main_layout = QHBoxLayout()
    left_layout = QVBoxLayout()
    right_layout = QHBoxLayout()

    toolbox = ToolBox()
    toolbox.setToolTip("Find all items here.")

    left_layout.addWidget(toolbox)
    left_layout.setAlignment(Qt.AlignLeft)

    main_layout.addLayout(left_layout)

    table = TabWidget()
    table.setMinimumWidth(800)
    main_layout.addWidget(table)
    main_layout.setContentsMargins(0, 5, 0, 0)

    right_layout.addWidget(right_up_text_edit(self))
    right_layout.addWidget(right_down_text_edit(self))

    main_layout.addLayout(right_layout)

    widget = QWidget()
    widget.setLayout(main_layout)
    self.setCentralWidget(widget)
