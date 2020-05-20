from PyQt5.QtWidgets import QVBoxLayout, QWidget, QGridLayout, QLineEdit, QApplication, QPushButton, QStyleFactory


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setMaximumSize(500, 300)
        self.setLayout(QVBoxLayout())
        self.result_field = QLineEdit()
        self.temp_nums = []
        self.fin_nums = []

        self.keypad()

        self.show()

    # noinspection PyArgumentList
    def keypad(self):
        container = QWidget()
        container.setLayout(QGridLayout())

        btn_result = QPushButton('Enter', clicked=self.func_result)
        btn_clear = QPushButton('Clear', clicked=self.clear_calc)

        btn_0 = QPushButton('0', clicked=lambda: self.num_press('0'))
        btn_1 = QPushButton('1', clicked=lambda: self.num_press('1'))
        btn_2 = QPushButton('2', clicked=lambda: self.num_press('2'))
        btn_3 = QPushButton('3', clicked=lambda: self.num_press('3'))
        btn_4 = QPushButton('4', clicked=lambda: self.num_press('4'))
        btn_5 = QPushButton('5', clicked=lambda: self.num_press('5'))
        btn_6 = QPushButton('6', clicked=lambda: self.num_press('6'))
        btn_7 = QPushButton('7', clicked=lambda: self.num_press('7'))
        btn_8 = QPushButton('8', clicked=lambda: self.num_press('8'))
        btn_9 = QPushButton('9', clicked=lambda: self.num_press('9'))

        btn_add = QPushButton('+', clicked=lambda: self.func_press('+'))
        btn_min = QPushButton('-', clicked=lambda: self.func_press('-'))
        btn_div = QPushButton('/', clicked=lambda: self.func_press('/'))
        btn_mul = QPushButton('*', clicked=lambda: self.func_press('*'))
        btn_exit = QPushButton('Exit', clicked=lambda: MainWindow.destroy())

        container.layout().addWidget(self.result_field, 0, 0, 1, 4)
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_add, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_min, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mul, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_div, 5, 3)
        container.layout().addWidget(btn_exit, 6, 0, 1, 4)
        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += '='
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


if __name__ == '__main__':
    app = QApplication([])
    app.setStyle(QStyleFactory.create('Fusion'))
    mw = MainWindow()
    app.exec_()
