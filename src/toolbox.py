from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QLabel, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table = ToolBox(self)
        self.setCentralWidget(self.table)

        self.show()


class ToolBox(QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolBox, self).__init__(*args, **kwargs)

        # self.setStyleSheet('background-color:yellow')
        layout = QVBoxLayout()
        toolbox = QToolBox()

        toolbox.setItemToolTip(0, 'This is a tooltip')

        layout.addWidget(toolbox)

        label1 = QLabel()
        toolbox.addItem(label1, 'One')

        label2 = QLabel()
        toolbox.addItem(label2, 'Two')

        label3 = QLabel()
        toolbox.addItem(label3, 'Three')

        label4 = QLabel()
        toolbox.addItem(label4, 'Four')

        label5 = QLabel()
        toolbox.addItem(label5, 'Five')

        label6 = QLabel()
        toolbox.addItem(label6, 'Six')

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
