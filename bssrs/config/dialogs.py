from PyQt5.Qt import Qt
from PyQt5.QtCore import QDateTime
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import (QDialog, QPushButton, QLabel, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout,
                             QLineEdit, QComboBox, QSpinBox, QDateEdit, QGridLayout, QTabWidget, QWidget)

from bssrs import __version__


class Dialogs(QDialog):
    def __init__(self):
        super(Dialogs, self).__init__()

        self.show_dialog()
        self.version_info()
        self.mainitemsdb()

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

    def mainitemsdb(self):
        d = QDialog()
        d.setMinimumSize(800, 600)
        d.setWindowTitle("Main ITEMS db")

        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addWidget(d)

        # d.setWindowModality(Qt.ApplicationModal)
        d.exec_()

    def notok(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())


#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     w = Dialogs()
#     w.show()
#     sys.exit(app.exec_())


class CustomerDialog(QDialog):

    def __init__(self):
        super(CustomerDialog, self).__init__()
        self.createFormGroupBox()

        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel | QDialogButtonBox.Reset)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.formGroupBox)
        main_layout.addWidget(button_box)

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Name:"), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)


# ==========================================================================


class CustomerDatabase(QDialog):
    def __init__(self, *args, **kwargs):
        super(CustomerDatabase, self).__init__(*args, **kwargs)

        self.setMinimumSize(300, 500)
        self.setWindowTitle("Customer Info‍")
        layout = QVBoxLayout()

        self.formGroupBox = QGroupBox("Customer Database")

        button_box = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel | QDialogButtonBox.Reset | QDialogButtonBox.Discard)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(self.formGroupBox)
        layout.addWidget(button_box)

        form_layout = QGridLayout()
        form_layout.setSpacing(20)
        form_layout.setContentsMargins(10, 10, 10, 10)

        self.fname = QLineEdit()
        self.fname.setPlaceholderText("First Name")
        self.fname.setFocus()

        self.lname = QLineEdit()
        self.lname.setPlaceholderText("Last Name")

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
