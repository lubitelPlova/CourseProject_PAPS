# import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import AdminWindow

class AdminWidget(QtWidgets.QMainWindow, AdminWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
