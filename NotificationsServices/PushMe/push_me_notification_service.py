import requests

from NotificationsServices.notification_service import NotificationService


class PushMeNotificationService(NotificationService):

    def __init__(self, device_identifier):
        super().__init__(device_identifier)
        self._service_url = 'https://pushmeapi.jagcesar.se'

    def send_test_notification(self):
        data = {'token': self.device_identifier, 'message': 'Test - Test'}
        requests.post(self._service_url, data)

    def send_notification(self, title, message):
        data = {'token': self.device_identifier, 'title': title + ' - ' + message}
        requests.post(self._service_url, data)

    @staticmethod
    def get_service_name():
        return 'PushMe'
