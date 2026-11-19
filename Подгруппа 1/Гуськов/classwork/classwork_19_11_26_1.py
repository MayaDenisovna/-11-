class Notification():
    def __init__(self, message):
        self.message = message

    def send(self):
        print(f'[!] сообщение готовится к отправке {self.message}')


class EmailNotification(Notification):
    def __init__(self, message, email_address):
        super().__init__(message)
        self.email_address = email_address

    def send(self):
        print(f'[!] сообщение "{self.message}" отправлено на почту {self.email_address}')


class SMSNotification(Notification):
    def __init__(self, message, phone_number):
        super().__init__(message)
        self.phone_number = phone_number

    def send(self):
        print(f'[!] сообщение "{self.message}" отправлено по смс на {self.phone_number}')


class PushNotification(Notification):
    def __init__(self, message, device):
        super().__init__(message)
        self.device = device

    def send(self):
        print(f'[!] пуш уведомление "{self.message}" на устройство {self.device}')


email = EmailNotification('Здравствуйте.', 'kuku@gmail.com')
sms1 = SMSNotification('Привет!', '+7 670 670 67 67')
sms2 = SMSNotification('Как дела?', '+7 (777) 777-77-77')
push1 = PushNotification('Реклама...', 'Телефон')
push2 = PushNotification('Напоминание...', 'Умные часы')


def send_all(listt):
    for i in listt:
        i.send()


send_all([email, sms1, sms2, push1, push2])
