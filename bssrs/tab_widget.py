import datetime
import sys

from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QLineEdit, QHBoxLayout, QPushButton, \
    QGridLayout, QLabel, QDateEdit, QComboBox

from bssrs.config.dialogs import show_dialog
from bssrs.config.messages import showdialog, customer_added
from bssrs.database.database_main import Database

font18 = QFont("Calibri", 18)

data = {
    'Garder': ["7'", "8'", "9'"],
    'Plates': ["3'-6\"","3'-9\"","3'-12\""],
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
    db = Database()

    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)

        self.edit_fname = QLineEdit()
        self.edit_lname = QLineEdit()
        self.edit_father = QLineEdit()
        self.edit_gender = QLineEdit()
        self.edit_street = QLineEdit()
        self.edit_city = QLineEdit()
        self.edit_pincode = QLineEdit()
        self.edit_number = QLineEdit()
        self.edit_email = QLineEdit()
        self.edit_careof = QLineEdit()
        self.edit_creation_date = QDateEdit(date=datetime.datetime.today())

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
        container = QGridLayout()
        container.setSpacing(20)
        container.setContentsMargins(10, 10, 10, 10)

        label_fname = QLabel("First Name:")
        label_lname = QLabel("Last Name:")
        label_father = QLabel("Father Name:")
        label_gender = QLabel("Gender:")
        label_street = QLabel("Street:")
        label_city = QLabel("City:")
        label_pincode = QLabel("PinCode:")
        label_number = QLabel("Mobile Number:")
        label_email = QLabel("Email:")
        label_careof = QLabel("Care of:")
        label_creation_date = QLabel("Date: ")

        container.layout().addWidget(label_fname, 0, 0)
        container.layout().addWidget(self.edit_fname, 0, 1)
        container.layout().addWidget(label_lname, 0, 2)
        container.layout().addWidget(self.edit_lname, 0, 3)

        container.layout().addWidget(label_father, 1, 0)
        container.layout().addWidget(self.edit_father, 1, 1)

        container.layout().addWidget(label_gender, 2, 0)
        container.layout().addWidget(self.edit_gender, 2, 1)

        container.layout().addWidget(label_street, 3, 0)
        container.layout().addWidget(self.edit_street, 3, 1)

        container.layout().addWidget(label_city, 3, 2)
        container.layout().addWidget(self.edit_city, 3, 3)

        container.layout().addWidget(label_pincode, 3, 4)
        container.layout().addWidget(self.edit_pincode, 3, 5)

        container.layout().addWidget(label_number, 4, 0)
        container.layout().addWidget(self.edit_number, 4, 1)

        container.layout().addWidget(label_email, 5, 0)
        container.layout().addWidget(self.edit_email, 5, 1)

        container.layout().addWidget(label_careof, 6, 0)
        container.layout().addWidget(self.edit_careof, 6, 1)

        container.layout().addWidget(label_creation_date, 6, 2)
        container.layout().addWidget(self.edit_creation_date, 6, 3)

        bottom_layout = QHBoxLayout()

        button_save = QPushButton('Save')
        button_save.setMinimumHeight(50)
        button_save.setFont(font18)
        button_save.clicked.connect(self.save_customer)

        button_reset = QPushButton('Reset')
        button_reset.setMinimumHeight(50)
        button_reset.setFont(font18)
        button_reset.clicked.connect(self.view_all_customers)

        button_delete = QPushButton('Delete')
        button_delete.setMinimumHeight(50)
        button_delete.setFont(font18)
        button_delete.clicked.connect(showdialog)

        button_edit = QPushButton('Edit')
        button_edit.setMinimumHeight(50)
        button_edit.setFont(font18)
        button_edit.clicked.connect(show_dialog)

        bottom_layout.layout().addWidget(button_save)
        bottom_layout.layout().addWidget(button_reset)
        bottom_layout.layout().addWidget(button_edit)
        bottom_layout.layout().addWidget(button_delete)

        container.addLayout(bottom_layout, 7, 0, 1, 6)
        self.tab1.setLayout(container)

    def save_customer(self):
        fname, lname, father, gender, street, city, pincode, number, email, careof, creation_date = self.edit_fname.text(), self.edit_lname.text(), self.edit_father.text(), self.edit_gender.text(), self.edit_street.text(), self.edit_city.text(), self.edit_pincode.text(), self.edit_number.text(), self.edit_email.text(), self.edit_careof.text(), self.edit_creation_date.text()
        print(fname, lname, father, gender, street, city, pincode, number, email, careof, creation_date)
        self.db.insert_customer(fname, lname, father, gender, street, city, pincode, number, email, careof,
                                creation_date)
        return customer_added(self, fname, lname, creation_date)

    def view_all_customers(self):
        m = TabWidget.db.view_all_customers()
        for x in m:
            print(x)

    def tab2ui(self):
        main_layout = QHBoxLayout()

        self.model = QStandardItemModel()

        self.lbl = QLabel("1.")
        self.lbl.setFont(font18)
        self.lbl.setMaximumWidth(30)

        self.edit_qty = QLineEdit()
        self.edit_qty.setFont(font18)
        self.edit_qty.setMaximumWidth(50)

        # states
        self.comboStates = QComboBox()
        self.comboStates.setFont(font18)
        self.comboStates.setModel(self.model)

        # cities
        self.comboCities = QComboBox()
        self.comboCities.setFont(font18)
        self.comboCities.setModel(self.model)

        self.btn_ok = QPushButton("OK")
        self.btn_ok.setFont(font18)
        self.btn_ok.setMaximumWidth(150)

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
        main_layout.addWidget(self.btn_ok)
        main_layout.addWidget(self.btn_cancel)
        self.tab2.setLayout(main_layout)

    def updateStateCombo(self, index):
        indx = self.model.index(index, 0, self.comboStates.rootModelIndex())
        self.comboCities.setRootModelIndex(indx)
        self.comboCities.setCurrentIndex(0)

    def tab3ui(self):
        return working_soon(self)

    def tab4ui(self):
        return working_soon(self)

    def tab5ui(self):
        return working_soon(self)


class GraphWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(GraphWidget, self).__init__(*args, **kwargs)

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
