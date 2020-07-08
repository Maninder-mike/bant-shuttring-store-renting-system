import sys

from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QDialog, QPushButton, QLabel, QDialogButtonBox, QVBoxLayout, QGroupBox, QFormLayout,
                             QLineEdit, QComboBox, QSpinBox, QApplication)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Dialogs()
    w.show()
    sys.exit(app.exec_())


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


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("STDMGMT")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/logo.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel("Version 5.3.2"))
        layout.addWidget(QLabel("Copyright 2018 CYB Inc."))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
