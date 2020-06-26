import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QStyleFactory, QTabWidget, QHBoxLayout, QLabel, QWidget

font18 = QFont("Calibri", 18)

data = {
    'Garder': ["7'", "8'", "9'"],
    'Plates': ["3'-6\"", "3'-9\"", "3'-12\""],
    'Texas': ['Austin', 'Houston', 'San Antonio']
}


def working_soon(self):
    container = QHBoxLayout()
    container.setSpacing(20)
    container.setContentsMargins(10, 10, 10, 10)

    label = QLabel("This Tab not working yet, Work in Progress ❤".upper())
    label.setFont(font18)
    container.layout().addWidget(label)
    self.tab2.setLayout(container) or self.tab3.setLayout(container) or self.tab4.setLayout(
        container) or self.tab5.setLayout(container)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table = TabWidget(self)
        self.setCentralWidget(self.table)

        self.show()


class TabWidget(QTabWidget):

    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)
        self.setMinimumSize(600, 600)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Contact Details')
        self.addTab(self.tab2, 'History')
        self.addTab(self.tab3, 'Bills')
        self.addTab(self.tab4, 'Pending Items')
        self.addTab(self.tab5, 'Offers')

        self.tab1ui()
        self.tab2ui()
        self.tab3ui()
        self.tab4ui()
        self.tab5ui()

    def tab1ui(self):
        return working_soon(self)

    def tab2ui(self):
        return working_soon(self)

    def tab3ui(self):
        return working_soon(self)

    def tab4ui(self):
        return working_soon(self)

    def tab5ui(self):
        return working_soon(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('windowsvista'))
    win = MainWindow()
    sys.exit(app.exec_())
