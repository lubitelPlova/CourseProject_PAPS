import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
 # Это наш конвертированный файл дизайна
from WindowFactory import AuthWindowFactory, AdminWindowFactory, MainWindowFactory



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = AuthWindowFactory.create_window()
    adminWindow = AdminWindowFactory.create_window()
    mainWindow = MainWindowFactory.create_window()
    AuthWindowFactory.setMainAdmin(window, mainWindow, adminWindow)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()