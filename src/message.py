
from abc import ABC, abstractmethod

class Message(ABC):
    def __init__(self, title, text):
        self.title = title
        self.text = text

    @abstractmethod
    def send(self):
        pass

class NotificationMessage(Message):
    def __init__(self, title, text, user_id):
        super().__init__(title, text)
        self.user_id = user_id

    def send(self):
        # Send notification to server
        import requests
        response = requests.post("http://localhost:5000/notifications", json={
            "user_id": self.user_id,
            "title": self.title,
            "message": self.text
        })
        if response.status_code == 201:
            print("Уведомление отправлено!")
        else:
            print("Ошибка отправки уведомления!")

        return response.status_code

class MessageCreator(ABC):
    @abstractmethod
    def create_message(self, title, text, **kwargs):
        pass

class NotificationMessageCreator(MessageCreator):
    def create_message(self, title, text, user_id):
        return NotificationMessage(title, text, user_id)
