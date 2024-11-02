from login_model import LoginModel

class LoginViewModel:
    def __init__(self):
        self.model = LoginModel()

    def get_login(self):
        return self.model.get_login()
    
    def get_password(self):
        return self.model.get_password()

    def set_login(self, login):
        self.model.set_login(login)

    def set_password(self, password):
        self.model.set_password(password)

    def check_credentials(self):
        return self.model.check_credentials()