from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QFormLayout, QLineEdit, QHBoxLayout
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table = TabWidget(self)
        self.setCentralWidget(self.table)

        self.show()


class TabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Tab 1')
        self.addTab(self.tab2, 'Tab 2')
        self.addTab(self.tab3, 'Tab 3')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QFormLayout()
        layout.addRow('Name', QLineEdit())
        layout.addRow('Address', QLineEdit())
        self.setTabText(0, 'Contact Details')
        self.tab1.setLayout(layout)

    def tab2UI(self):
        pass

    def tab3UI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
