from PyQt5 import QtWidgets
import requests
from message import NotificationMessageCreator

class NotificationWindow(QtWidgets.QMainWindow): #
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Уведомления")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget to hold the layout
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        # Create the layout
        self.layout = QtWidgets.QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.notifications_list = QtWidgets.QListWidget()
        self.layout.addWidget(self.notifications_list)

        self.create_notification_group = QtWidgets.QWidget()
        self.layout.addWidget(self.create_notification_group)

        self.create_notification_layout = QtWidgets.QVBoxLayout()
        self.create_notification_group.setLayout(self.create_notification_layout)

        self.title_input = QtWidgets.QLineEdit()
        self.title_input.setPlaceholderText("Заголовок")
        self.create_notification_layout.addWidget(self.title_input)

        self.text_input = QtWidgets.QTextEdit()
        self.text_input.setPlaceholderText("Текст")
        self.create_notification_layout.addWidget(self.text_input)

        self.recipients_combo = QtWidgets.QComboBox()
        self.recipients_combo.addItems(["Группа 1", "Группа 2", "Группа 3"])
        self.create_notification_layout.addWidget(self.recipients_combo)

        self.send_button = QtWidgets.QPushButton("Отправить")
        self.send_button.clicked.connect(self.send_notification)
        self.create_notification_layout.addWidget(self.send_button)

        self.error_label = QtWidgets.QLabel()
        self.error_label.setStyleSheet("color: red")
        self.create_notification_layout.addWidget(self.error_label)

        self.get_notifications()

    def send_notification(self):
        title = self.title_input.text()
        text = self.text_input.toPlainText()
        recipients = self.recipients_combo.currentText()

        

        if not title:
            self.error_label.setText("Введите заголовок!")
            return

        creator = NotificationMessageCreator()
        message = creator.create_message(title, text, user_id=1)
        response_code = message.send()

        print(response_code)
        if response_code == 201:
            self.error_label.setText("Уведомление отправлено!")
            self.get_notifications()
        else:
            self.error_label.setText("Ошибка отправки уведомления!")

        # Clear input fields
        self.title_input.clear()
        self.text_input.clear()


    def get_notifications(self):
        # Get notifications from server
        response = requests.get("http://localhost:5000/notifications?user_id=1")  # Replace with actual user ID

        if response.status_code == 200:
            notifications = response.json()["notifications"]
            self.notifications_list.clear()
            for notification in notifications:
                self.notifications_list.addItem(f"{notification['title']} - {notification['message']}")
        else:
            self.error_label.setText("Ошибка получения уведомлений!")