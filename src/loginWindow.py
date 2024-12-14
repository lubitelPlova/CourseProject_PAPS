from PyQt5 import QtWidgets
import auth
import requests

class LoginWindow(QtWidgets.QMainWindow, auth.Ui_MainWindow):
    mainWindow = None
    adminWindow = None
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле auth.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.enterButton.clicked.connect(self.check_credentials)


    def check_credentials(self):
        login = self.viewModel.get_login()
        password = self.viewModel.get_password()
        # print(type(login))
        response = requests.post("http://localhost:5000/login", json={"login": login, "password": password})
        if response.status_code == 200:  # проверяем, что запрос был успешным
            try:
                data = response.json()
                print(data)
                if "success" in data and data["success"] and data["admin"] != True:
                    # Открытие пользовательского
                    # self.mainWindow = MainWindowFactory.create_window()
                    print("Not admin")
                    self.mainWindow.show()
                    self.close()
                    return 1
                elif "success" in data and data["success"] and data["admin"] == True:
                    # self.adminWindow = AdminWindowFactory.create_window()
                    print("admin")
                    self.adminWindow.show()
                    self.close()
                    #открытие админского окна
                else:
                    print("Неправильный логин или пароль!")
            except ValueError:  # если ответ не в формате JSON
                print("Ошибка формата ответа")
        else:
            print("Ошибка сервера")
