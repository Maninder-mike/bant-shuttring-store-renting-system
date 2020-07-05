import sys
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QToolBox, QLabel, QMainWindow, QLineEdit, QTextEdit, \
    QPushButton


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.table = ToolBox(self)
        self.setCentralWidget(self.table)

        self.show()


class ToolBox(QWidget):
    def __init__(self, *args, **kwargs):
        super(ToolBox, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        toolbox = QToolBox()
        layout.setAlignment(Qt.AlignLeft)
        toolbox.setMaximumWidth(300)

        layout.addWidget(toolbox)

        folder = QIcon("images/imageres.ico")

        w1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Garder 7'"))
        layout1.addWidget(QLabel("Garder 8'"))
        layout1.addWidget(QLabel("Garder 9'"))
        layout1.addWidget(QLabel("Garder 10'"))
        layout1.addWidget(QLabel("Garder 11'"))
        layout1.addWidget(QLabel("Garder 12'"))
        layout1.addWidget(QLabel("Garder 13'"))
        layout1.addWidget(QLabel("Garder 14'"))
        layout1.addWidget(QLabel("Garder 15'"))
        layout1.addWidget(QLabel("Garder 16'"))
        layout1.addWidget(QLabel("Garder 17'"))
        layout1.addWidget(QLabel("Garder 18'"))
        layout1.addWidget(QLabel("Garder 19'"))
        layout1.addWidget(QLabel("Garder 20'"))
        w1.setLayout(layout1)
        toolbox.addItem(w1, folder,'Garder')

        w2 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Plates 3'-6\""))
        layout1.addWidget(QLabel("Plates 3'-9\""))
        layout1.addWidget(QLabel("Plates 3'-12\""))
        layout1.addWidget(QLabel("Plates 3'-15\""))
        layout1.addWidget(QLabel("Plates 3'-18\""))
        layout1.addWidget(QLabel("Plates 4'-6\""))
        layout1.addWidget(QLabel("Plates 4'-9\""))
        layout1.addWidget(QLabel("Plates 4'-12\""))
        layout1.addWidget(QLabel("Plates 4'-15\""))
        layout1.addWidget(QLabel("Plates 4'-18\""))
        w2.setLayout(layout1)
        toolbox.addItem(w2, folder,'Plates')

        w3 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Spota 7'"))
        layout1.addWidget(QLabel("Spota 8'"))
        layout1.addWidget(QLabel("Spota 9'"))
        layout1.addWidget(QLabel("Spota 10'"))
        layout1.addWidget(QLabel("Spota 11'"))
        layout1.addWidget(QLabel("Spota 12'"))
        layout1.addWidget(QLabel("Spota 13'"))
        layout1.addWidget(QLabel("Spota 14'"))
        layout1.addWidget(QLabel("Spota 15'"))
        layout1.addWidget(QLabel("Spota 16'"))
        layout1.addWidget(QLabel("Spota 17'"))
        layout1.addWidget(QLabel("Spota 18'"))
        layout1.addWidget(QLabel("Spota 19'"))
        layout1.addWidget(QLabel("Spota 20'"))
        layout1.addWidget(QLabel("Spota 21'"))
        layout1.addWidget(QLabel("Spota 22'"))
        layout1.addWidget(QLabel("Spota 23'"))
        layout1.addWidget(QLabel("Spota 24'"))
        layout1.addWidget(QLabel("Spota 25'"))
        w3.setLayout(layout1)
        toolbox.addItem(w3, folder,'Spota')

        # tab X
        w = QWidget()
        layout1 = QVBoxLayout()
        self.lineEdit = QLineEdit()
        layout1.addWidget(QLabel('Enter something'))
        layout1.addWidget(self.lineEdit)
        w.setLayout(layout1)

        toolbox.addItem(w, 'Tab X')

        # tab Y
        btn = QPushButton('My Button')
        btn.clicked.connect(self.printText)
        toolbox.addItem(btn, 'Tab Y')

        # tab Z
        self.textEditor = QTextEdit()
        toolbox.addItem(self.textEditor, 'Tab Z')
        toolbox.setCurrentIndex(1)

        self.setLayout(layout)

    def printText(self):
        self.textEditor.setPlainText(self.lineEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
