from NotificationService import NotificationService
from pushover_complete import PushoverAPI


class PushoverNotificationService(NotificationService):

    def __init__(self, api_key, device_identifier):
        super().__init__(api_key, device_identifier)
        self._notification_service = PushoverAPI(self._api_key)

    def send_test_notification(self):
        self._notification_service.send_message(self.device_identifier, 'Test', title='Test')

    def send_notification(self, title, message):
        self._notification_service.send_message(self.device_identifier, message, title=title)

    def get_service_name(self):
        return 'Pushover'
