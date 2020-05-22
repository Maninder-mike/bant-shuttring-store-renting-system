from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QVBoxLayout
import sys
from src.toolbox import ToolBox
from src.tab_widget import TabWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setMinimumSize(500, 500)

        self.layout = Layout()
        self.setCentralWidget(self.layout)

        self.show()


class Layout(QWidget):

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
