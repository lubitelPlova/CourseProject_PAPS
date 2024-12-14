from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget
from loginWindow import LoginWindow
from workspace_window import WorkspaceWindow
from AdminWidget import AdminWidget
from notification_window import NotificationWindow

class WindowFactory(ABC):
    @abstractmethod
    def create_window(self) -> QWidget: #QWidget - абстрактный класс окна, описанный в PyQt
        pass

class AuthWindowFactory(WindowFactory): #Конкретная реализация окна логина
    def create_window() -> QWidget:
        return LoginWindow()
    
    def setMainAdmin(log: LoginWindow, main, admin):
        log.mainWindow = main
        log.adminWindow = admin
    
class MainWindowFactory(WindowFactory): #Конкретная реализация главного окна
    def create_window() -> QWidget:
        return WorkspaceWindow()
    
class AdminWindowFactory(WindowFactory): #Конкретная реализация окна администратора
    def create_window() -> QWidget:
        return AdminWidget()
    
class NotificationWindowFactory(WindowFactory):
    def create_window(self) -> QWidget:
        return NotificationWindow()