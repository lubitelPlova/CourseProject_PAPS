from PyQt5 import QtWidgets
from workspace import Ui_WorkspaceWindow

class WorkspaceWindow(QtWidgets.QMainWindow, Ui_WorkspaceWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)