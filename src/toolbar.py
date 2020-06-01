from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class ToolBar(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ToolBar, self).__init__(*args, **kwargs)
        self.setMinimumSize(500, 500)

        self.tool_bar()
        self.show()

    def tool_bar(self):
        edit_toolbar = self.addToolBar('Edit')
        edit_toolbar.addAction('Undo')
        edit_toolbar.addAction('Redo')
        edit_toolbar.addAction('Cut')
        edit_toolbar.addAction('Copy')
        edit_toolbar.addAction('Paste')

        view_toolbar = self.addToolBar('View')
        view_toolbar.addAction('Themes')
        view_toolbar.addAction('Recent Files')
        view_toolbar.addAction('Location')
        view_toolbar.addAction('Contact Info')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ToolBar()
    sys.exit(app.exec_())
