from PyQt5.QtWidgets import QLineEdit, QCompleter


def tool_bar(self):
    edit_toolbar = self.addToolBar('Edit')
    edit_toolbar.setFixedHeight(30)
    edit_toolbar.addAction('Undo')
    edit_toolbar.addAction('Redo')
    edit_toolbar.addAction('Cut')
    edit_toolbar.addAction('Copy')
    edit_toolbar.addAction('Paste')
    edit_toolbar.addSeparator()

    view_toolbar = self.addToolBar('View')
    view_toolbar.addAction('Themes')
    view_toolbar.addAction('Recent Files')
    view_toolbar.addAction('Location')
    view_toolbar.addAction('Contact Info')
    view_toolbar.addSeparator()

    sample = ["Apple", "Alps", "Berry", "Cherry"]
    completer = QCompleter(sample)

    search_toolbar = self.addToolBar('Search')
    search = QLineEdit()
    search_toolbar.addWidget(search)
    search.setCompleter(completer)

    search_toolbar.setFixedWidth(300)
    search_toolbar.setToolTip("Search all data, names, dates, and bills")
    search_toolbar.addSeparator()
    search_toolbar.addAction("Search")
