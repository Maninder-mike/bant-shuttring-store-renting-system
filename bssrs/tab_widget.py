import json
import sys

from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTabWidget, QLineEdit, QHBoxLayout, QPushButton,
                             QLabel, QComboBox)

from bssrs.database.database_main import Database

font18 = QFont("Calibri", 18)

with open('database/notouch_database.json', 'r')as f:
    file = json.load(f)


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
    db = Database()

    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Main')
        self.addTab(self.tab2, 'Contacts')
        self.addTab(self.tab3, 'Bills')
        self.addTab(self.tab4, 'Pending Items')
        self.addTab(self.tab5, 'Offers')

        self.tab1ui()
        self.tab2ui()
        self.tab3ui()
        self.tab4ui()
        self.tab5ui()

    def tab1ui(self):

        main_layout = QHBoxLayout()

        main_layout.setAlignment(Qt.AlignTop)
        self.model = QStandardItemModel()

        self.lbl = QLabel("1.")
        self.lbl.setFont(font18)
        self.lbl.setMaximumWidth(30)

        self.edit_qty = QLineEdit()
        self.edit_qty.setFont(font18)
        self.edit_qty.setMaximumWidth(50)
        self.edit_qty.setFocus()

        # states
        self.comboStates = QComboBox()
        self.comboStates.setFont(font18)
        self.comboStates.setModel(self.model)

        # cities
        self.comboCities = QComboBox()
        self.comboCities.setFont(font18)
        self.comboCities.setModel(self.model)

        self.edit_rate = QLineEdit()
        self.edit_rate.setFont(font18)
        self.edit_rate.setText("1.5")
        self.edit_rate.setMaximumWidth(50)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.setFont(font18)
        self.btn_ok.setMaximumWidth(150)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setFont(font18)
        self.btn_cancel.setMaximumWidth(150)

        # add data
        for k, v in file.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in str(v):
                size = QStandardItem(value)
                state.appendRow(size)

        self.comboStates.currentIndexChanged.connect(self.updateStateCombo)
        self.updateStateCombo(0)

        main_layout.addWidget(self.lbl)
        main_layout.addWidget(self.edit_qty)
        main_layout.addWidget(self.comboStates)
        main_layout.addWidget(self.comboCities)
        main_layout.addWidget(self.edit_rate)
        main_layout.addWidget(self.btn_ok)
        main_layout.addWidget(self.btn_cancel)
        self.tab1.setLayout(main_layout)

    def updateStateCombo(self, index):
        indx = self.model.index(index, 0, self.comboStates.rootModelIndex())
        self.comboCities.setRootModelIndex(indx)
        self.comboCities.setCurrentIndex(0)

    def tab2ui(self):
        mlayout = QHBoxLayout()
        mlayout.setAlignment(Qt.AlignTop)

        def click():
            for x in range(1, 3):
                btn = QPushButton(str(x))
                mlayout.addWidget(btn)
            for _ in range(1, 3):
                edit = QLineEdit()
                edit.setPlaceholderText('text edit')
                mlayout.addWidget(edit)

        click()

        self.tab2.setLayout(mlayout)

    def tab3ui(self):
        return working_soon(self)

    def tab4ui(self):
        return working_soon(self)

    def tab5ui(self):
        return working_soon(self)


class GraphWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(GraphWidget, self).__init__(*args, **kwargs)

        self.setTabPosition(QTabWidget.South)

        self.tab1 = QWidget()
        self.tab1.setToolTip("Graph window")
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Income')
        self.addTab(self.tab2, 'Expensive')
        self.addTab(self.tab3, 'Report')

        self.graph_tab1()
        self.graph_tab2()
        self.graph_tab3()

    def graph_tab1(self):
        layout = QHBoxLayout()
        self.tab2.setLayout(layout)

    def graph_tab2(self):
        layout = QHBoxLayout()
        self.tab2.setLayout(layout)

    def graph_tab3(self):
        layout = QHBoxLayout()
        self.tab2.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
