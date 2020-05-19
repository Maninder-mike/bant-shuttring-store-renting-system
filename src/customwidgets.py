from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout


class OnOffWidget(QWidget):
    def __init__(self, name):
        super(OnOffWidget, self).__init__()
        self.name = name
        self.is_on = False

        self.lbl = QLabel(self.name)
        self.btn_on = QPushButton('On')
        self.btn_off = QPushButton('Off')

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.lbl)
        self.hbox.addWidget(self.btn_on)
        self.hbox.addWidget(self.btn_off)
        self.setLayout(self.hbox)

        self.btn_on.clicked.connect(self.on)
        self.btn_off.clicked.connect(self.off)

        self.update_btn_state()

    def off(self):
        self.is_on = False
        self.update_btn_state()

    def on(self):
        self.is_on = True
        self.update_btn_state()

    def update_btn_state(self):
        if self.btn_on:
            self.btn_on.setStyleSheet('background-color: #4CAF50; color: #fff')
            self.btn_off.setStyleSheet('background-color: none; color: none')
        else:
            self.btn_on.setStyleSheet('background-color: none; color: none')
            self.btn_off.setStyleSheet('background-color: #D32F2F; color: #fff')
