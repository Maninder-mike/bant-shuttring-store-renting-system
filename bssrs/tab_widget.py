import datetime
import sys
from random import randint

from PyQt5.Qt import Qt
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QTabWidget, QLineEdit, QHBoxLayout, QPushButton,
                             QGridLayout, QLabel, QDateEdit, QComboBox)

from bssrs.config.messages import customer_added
from bssrs.database.database_main import Database

font18 = QFont("Calibri", 18)

data = {
    'Garder': ["7'", "8'", "9'", "10'", "11'", "12'", "13'", "14'", "15'", "16'", "17'", "18'", "19'", "20'"],
    'Plates': ["3'-6\"", "3'-9\"", "3'-12\"", "3'-18\"", "3'-24\"", "4'-6\"", "4'-9\"", "4'-12\"", "4'-18\"", "4'-24\""]
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

        def check_disable():
            if self.edit_qty.text() == "":
                return self.btn_ok.setDisabled(True)
            else:
                return self.btn_ok.setDisabled(False)

        def change_lbl():
            def random121():
                return randint(0, 20)

            self.lbl.setText(str(random121()))

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

        self.edit_qty.textChanged.connect(check_disable)
        self.edit_rate.textChanged.connect(check_disable)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.setFont(font18)
        self.btn_ok.setMaximumWidth(150)
        self.btn_ok.clicked.connect(change_lbl)

        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.setFont(font18)
        self.btn_cancel.setMaximumWidth(150)

        # add data
        for k, v in data.items():
            state = QStandardItem(k)
            self.model.appendRow(state)
            for value in v:
                city = QStandardItem(value)
                state.appendRow(city)

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
        return working_soon(self)
        # container = QGridLayout()
        # container.setSpacing(20)
        # container.setContentsMargins(10, 10, 10, 10)
        # bottom_layout = QHBoxLayout()
        #
        # button_save = QPushButton('Save')
        # button_save.setMinimumHeight(50)
        # button_save.setFont(font18)
        # # button_save.clicked.connect(self.save_customer)
        #
        # button_reset = QPushButton('Reset')
        # button_reset.setMinimumHeight(50)
        # button_reset.setFont(font18)
        # # button_reset.clicked.connect(self.view_all_customers)
        #
        # button_delete = QPushButton('Delete')
        # button_delete.setMinimumHeight(50)
        # button_delete.setFont(font18)
        #
        # button_edit = QPushButton('Edit')
        # button_edit.setMinimumHeight(50)
        # button_edit.setFont(font18)
        #
        # bottom_layout.layout().addWidget(button_save)
        # bottom_layout.layout().addWidget(button_reset)
        # bottom_layout.layout().addWidget(button_edit)
        # bottom_layout.layout().addWidget(button_delete)
        #
        # container.addLayout(bottom_layout, 7, 0, 1, 6)
        # self.tab2.setLayout(container)


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
