import sys
import json
from PyQt5.Qt import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QToolBox, QLabel, QMainWindow, QLineEdit, QTextEdit,
                             QPushButton)

with open('../notouch_database.json', 'r') as f:
    file = json.load(f)
    garder_list = []
    plates_list = []
    spot_list = []
    fatta_list = []
    godi_list = []
    podi_list = []
    for x in file['garder'].values():
        garder_list.append(x)
    for y in file['plate'].values():
        plates_list.append(x)
    for z in file['spot'].values():
        spot_list.append(z)
    for m in file['fatta'].values():
        fatta_list.append(m)
    for n in file['godi'].values():
        godi_list.append(n)
    for o in file['podi'].values():
        podi_list.append(o)


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
        for c in file['garder'].keys():
            garder_lbl = QLabel(f'{c}')
            layout1.addWidget(garder_lbl)
        w1.setLayout(layout1)
        toolbox.addItem(w1, folder, f'ਗਾਡਰ - {sum(garder_list)}')

        w2 = QWidget()
        layout1 = QVBoxLayout()
        for b in file['plate'].keys():
            plate_lbl = QLabel(f'{b}')
            layout1.addWidget(plate_lbl)
        w2.setLayout(layout1)
        toolbox.addItem(w2, folder, f'ਪਲੇਟਾਂ - {sum(plates_list)}')

        w3 = QWidget()
        layout1 = QVBoxLayout()
        for a in file['spot'].keys():
            lbl = QLabel(f'{a}')
            layout1.addWidget(lbl)
        w3.setLayout(layout1)
        toolbox.addItem(w3, folder, f'ਸ਼ਪੋਂਟਾਂ - {sum(spot_list)}')

        w4 = QWidget()
        layout1 = QVBoxLayout()
        for d in file['fatta'].keys():
            lbl = QLabel(f'{d}')
            layout1.addWidget(lbl)
        w4.setLayout(layout1)
        toolbox.addItem(w4, folder, f'ਫੱਟਾਂ - {sum(fatta_list)}')

        w5 = QWidget()
        layout1 = QVBoxLayout()
        for e in file['godi'].keys():
            lbl = QLabel(f'{e}')
            layout1.addWidget(lbl)
        w5.setLayout(layout1)
        toolbox.addItem(w5, folder, f'ਘੋੜੀ - {sum(godi_list)}')

        w6 = QWidget()
        layout1 = QVBoxLayout()
        for g in file['podi'].keys():
            lbl = QLabel(f'{g}')
            layout1.addWidget(lbl)
        w6.setLayout(layout1)
        toolbox.addItem(w6, folder, f'ਪੌੜੀ - {sum(podi_list)}')

        w7 = QWidget()
        layout1 = QVBoxLayout()
        num = 1
        for h in file.keys():
            lbl = QLabel(f'{num}.  {h}')
            layout1.addWidget(lbl)
            num += 1
        w7.setLayout(layout1)
        toolbox.addItem(w7, folder, 'ਹੋਂਰ')

        toolbox.setCurrentIndex(0)
        self.setLayout(layout)

    def printText(self):
        self.textEditor.setPlainText(self.lineEdit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
