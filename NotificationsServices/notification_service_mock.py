import logging

from NotificationsServices.notification_service import NotificationService


class NotificationServiceMock(NotificationService):
    def __init__(self, device_identifier):
        super().__init__(device_identifier)
        self._notification_list = []
        self._counter = 1

    @staticmethod
    def get_service_name() -> str:
        raise NotImplementedError('Should have implemented this')

    def send_notification(self, title: str, message: str) -> None:
        self._notification_list.append({'message': message, 'title': title, 'number': self._counter})
        self._counter += 1
        logging.debug('%s Mock: Title: "%s" Message: "%s', self.get_service_name(), title, message)

    def send_test_notification(self) -> None:
        self.send_notification('Test', 'Test')

    def get_notification_list(self):
        return self._notification_list
