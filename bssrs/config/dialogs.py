import json

from PyQt5.Qt import Qt
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import (QDialog, QPushButton, QLabel, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout,
                             QLineEdit, QComboBox, QDateEdit, QGridLayout, QTabWidget, QWidget, QMessageBox,
                             QInputDialog, QHBoxLayout)

from bssrs import __version__
from bssrs.database.database_main import Database

db = Database()


class Dialogs(QDialog):

    def __init__(self):
        super(Dialogs, self).__init__()

    def show_dialog(self):
        d = QDialog()
        b1 = QPushButton("ok", d)
        b1.move(50, 50)
        d.setFixedSize(200, 200)
        d.setWindowTitle("Button Edit Window")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def version_info(self):
        d = QDialog()
        b1 = QPushButton(str(__version__), d)
        b1.move(50, 50)
        d.setFixedSize(200, 200)
        d.setWindowTitle("Button Edit Window")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()


class CustomerDatabase(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomerDatabase, self).__init__(*args, **kwargs)

        self.setMinimumSize(300, 500)
        self.setWindowTitle("Customer Info‍")
        layout = QVBoxLayout()

        self.formGroupBox = QGroupBox("Customer Database")

        button_box = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel | QDialogButtonBox.Reset)
        button_box.accepted.connect(self.add_customer)
        button_box.rejected.connect(self.close)
        button_box.clicked.connect(self.reset_customer)

        layout.addWidget(self.formGroupBox)
        layout.addWidget(button_box)

        form_layout = QGridLayout()
        form_layout.setSpacing(20)
        form_layout.setContentsMargins(10, 10, 10, 10)

        self.edit_fname = QLineEdit()
        self.edit_fname.setPlaceholderText("First Name")
        self.edit_lname = QLineEdit()
        self.edit_lname.setPlaceholderText("Last Name")
        self.edit_father = QLineEdit()
        self.edit_father.setPlaceholderText("Father Name")
        self.edit_gender = QComboBox()
        self.edit_gender.addItems(['Male', 'Female'])
        self.edit_street = QLineEdit()
        self.edit_street.setPlaceholderText("Street")
        self.edit_city = QLineEdit()
        self.edit_city.setPlaceholderText("City")
        self.edit_pincode = QLineEdit()
        self.edit_pincode.setPlaceholderText("Pincode")
        self.edit_number = QLineEdit()
        self.edit_number.setPlaceholderText("Phone Number")
        self.edit_email = QLineEdit()
        self.edit_email.setPlaceholderText("Email")
        self.edit_careof = QLineEdit()
        self.edit_careof.setPlaceholderText("Care Of")
        self.edit_creation_date = QDateEdit()
        self.edit_creation_date.setDateTime(QDateTime.currentDateTime())

        self.btn = QPushButton("Add Customer !!!")
        self.btn.clicked.connect(self.add_customer)

        form_layout.addWidget(self.edit_fname, 0, 1)
        form_layout.addWidget(self.edit_lname, 0, 3)
        form_layout.addWidget(self.edit_father, 1, 1)
        form_layout.addWidget(self.edit_gender, 2, 1)
        form_layout.addWidget(self.edit_street, 3, 1)
        form_layout.addWidget(self.edit_city, 3, 3)
        form_layout.addWidget(self.edit_pincode, 3, 5)
        form_layout.addWidget(self.edit_number, 4, 1)
        form_layout.addWidget(self.edit_email, 4, 3)
        form_layout.addWidget(self.edit_careof, 6, 1)
        form_layout.addWidget(self.edit_creation_date, 6, 3)
        form_layout.addWidget(self.btn, 6, 5)

        self.cbox = QComboBox()
        # self.cbox.addItems([str(x) for x in pm_Combo()])
        self.cbox.setEditable(True)
        self.cbox.setDisabled(True)

        self.age = QLineEdit()
        self.age.setPlaceholderText("Price")
        self.age.setValidator(QDoubleValidator())

        self.dateedit = QDateEdit()
        self.dateedit.setDateTime(QDateTime.currentDateTime())

        self.formGroupBox.setLayout(form_layout)

        self.setLayout(layout)

    def add_customer(self):
        if self.edit_fname.text() == "" and self.edit_lname.text() == "":
            QMessageBox.warning(self, "Warning : Please add all fields", "Don't empty fields 🤦🏽‍‍")
        else:
            db.insert_cust(self.edit_fname.text(), self.edit_lname.text(), self.edit_father.text(),
                           self.edit_gender.currentText(), self.edit_street.text(), self.edit_city.text(),
                           self.edit_pincode.text(), self.edit_number.text(), self.edit_email.text(),
                           self.edit_careof.text(), self.edit_creation_date.text())
            QMessageBox.information(self, "Added",
                                    f"{self.edit_fname.text()} {self.edit_lname.text()} added in {self.edit_creation_date.text()}")
            print("Data is Added!")

    def delete_customer(self):
        items = [str(x) for x in db.customer_list()]

        item, ok = QInputDialog.getItem(self, "Delete Customer", "This is Label", items, 0, False)
        if ok and items:
            return db.delete_cust(item)

    def print_line(self):
        print("Check Success <>")

    def discard_line(self):
        print("Discard Success <>")

    def reset_customer(self):
        return (self.edit_fname.clear(), self.edit_lname.clear(), self.edit_father.clear(), self.edit_street.clear(),
                self.edit_city.clear(), self.edit_pincode.clear(), self.edit_number.clear(), self.edit_email.clear(),
                self.edit_careof.clear())

    def dialog_window(self):
        dwin = CustomerDatabase()
        dwin.exec_()


class SettingWindow(QDialog):

    def __init__(self, *args, **kwargs):
        super(SettingWindow, self).__init__(*args, **kwargs)

        self.setMinimumSize(500, 500)
        self.setWindowTitle("Settings‍")

        layout = QVBoxLayout()
        layout.setSpacing(0)

        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, 'Font')
        self.tabs.addTab(self.tab2, 'BackUp')
        self.tabs.addTab(self.tab3, 'Internet')

        layout.addWidget(self.tabs)
        self.setLayout(layout)

    def settings_window(self):
        dwin = SettingWindow()
        dwin.exec_()


