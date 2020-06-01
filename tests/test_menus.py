import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QKeySequence, Qt
from src.main import MainWindow
from PyQt5.QtTest import QTest

# def test_open_proj_current_window():
#     with pytest_hackedit.MainWindow(PATH1, remove_project_folder=True) as w:
#         settings.set_open_mode(settings.OpenMode.CURRENT_WINDOW)
#         assert settings.open_mode() == settings.OpenMode.CURRENT_WINDOW
#         assert len(project.get_projects()) == 1
#         project.open_project(PATH2, sender=w.instance)
#         assert len(project.get_projects()) == 2
#         QtTest.QTest.qWait(1000)
