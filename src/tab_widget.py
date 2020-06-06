from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTabWidget, QFormLayout, QLineEdit, QHBoxLayout, \
    QPushButton, QGridLayout, QLabel, QVBoxLayout
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
        self.tab1.setToolTip("Contact window for client personal information")
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Tab 1')
        self.addTab(self.tab2, 'Tab 2')
        self.addTab(self.tab3, 'Tab 3')
        self.addTab(self.tab4, 'Tab 4')
        self.addTab(self.tab5, 'Tab 5')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        container = QGridLayout()
        container.setSpacing(20)
        container.setContentsMargins(10, 10, 10, 10)

        label_fname = QLabel("First Name:")
        label_lname = QLabel("Last Name:")
        label_father = QLabel("Father Name:")
        label_gender = QLabel("Gender:")
        label_street = QLabel("Street:")
        label_city = QLabel("City:")
        label_number = QLabel("Mobile Number:")
        label_email = QLabel("Email:")
        label_careof = QLabel("Care of:")

        edit_fname = QLineEdit()
        edit_lname = QLineEdit()
        edit_father = QLineEdit()
        edit_gender = QLineEdit()
        edit_street = QLineEdit()
        edit_city = QLineEdit()
        edit_number = QLineEdit()
        edit_email = QLineEdit()
        edit_careof = QLineEdit()

        container.layout().addWidget(label_fname, 0, 0)
        container.layout().addWidget(edit_fname, 0, 1)
        container.layout().addWidget(label_lname, 0, 2)
        container.layout().addWidget(edit_lname, 0, 3)

        container.layout().addWidget(label_father, 1, 0)
        container.layout().addWidget(edit_father, 1, 1)

        container.layout().addWidget(label_gender, 2, 0)
        container.layout().addWidget(edit_gender, 2, 1)

        container.layout().addWidget(label_street, 3, 0)
        container.layout().addWidget(edit_street, 3, 1)

        container.layout().addWidget(label_city, 3, 2)
        container.layout().addWidget(edit_city, 3, 3)

        container.layout().addWidget(label_number, 5, 0)
        container.layout().addWidget(edit_number, 5, 1)

        container.layout().addWidget(label_email, 6, 0)
        container.layout().addWidget(edit_email, 6, 1)

        container.layout().addWidget(label_careof, 7, 0)
        container.layout().addWidget(edit_careof, 7, 1)

        bottom_layout = QHBoxLayout()

        button_save = QPushButton('Save')
        button_reset = QPushButton('Reset')
        button_delete = QPushButton('Delete')
        button_edit = QPushButton('Edit')
        bottom_layout.layout().addWidget(button_save)
        bottom_layout.layout().addWidget(button_reset)
        bottom_layout.layout().addWidget(button_edit)
        bottom_layout.layout().addWidget(button_delete)

        container.addLayout(bottom_layout, 9, 0, 1, 4)

        self.setTabText(0, 'Contact Details')
        self.tab1.setLayout(container)

    def tab2UI(self):
        layout = QHBoxLayout()
        self.setTabText(1, 'History')
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        self.setTabText(2, 'Bills')
        self.tab2.setLayout(layout)

    def tab4UI(self):
        layout = QHBoxLayout()
        self.setTabText(3, 'Panding Items')
        self.tab2.setLayout(layout)

    def tab5UI(self):
        layout = QHBoxLayout()
        self.setTabText(4, 'Offers')
        self.tab2.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
