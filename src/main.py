import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout

try:
    from src.customwidgets import OnOffWidget
except:
    from customwidgets import OnOffWidget


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        container = QWidget()
        container_layout = QVBoxLayout()
        container.setLayout(container_layout)

        onoff = OnOffWidget('Testing')
        container_layout.addWidget(onoff)

        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
