from PyQt5.QtWidgets import QMessageBox


def showdialog(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("this is a long line comment man.")
    msg.setFixedSize(300,300)
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.buttonClicked.connect(msg_btn)

    msg.exec_()


def msg_btn(i):
    # print("Button pressed is:", i.text())
    if i.text() == "&Yes":
        print("you call Ok Bitch!")
    elif i.text() == "&No":
        print("No is here!")
    else:
        print(i.text())
