class LoginModel:
    def __init__(self):
        self.login = None
        self.password = None

    def set_login(self, login):
        self.login = login

    def get_login(self):
        return self.login

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def check_credentials(self):
        # Здесь будет логика проверки логина и пароля
        # Для примера, мы просто проверяем, что логин и пароль не пустые
        if ((self.login == "Dima") and (self.password == "Mazur")):
            return True
        else:
            return False
