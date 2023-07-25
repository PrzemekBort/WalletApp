from PyQt6.QtWidgets import QApplication
from src.gui.MainWindow import MainWindow


class MainApp(QApplication):

    def __init__(self, argv):
        super(MainApp, self).__init__(argv)
        self.ui = MainWindow()
        self.ui.show()
