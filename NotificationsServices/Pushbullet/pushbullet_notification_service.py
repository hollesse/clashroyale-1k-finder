import logging
from pushbullet.pushbullet import Pushbullet

from NotificationsServices.notification_service import NotificationService


class PushbulletNotificationservice(NotificationService):

    @staticmethod
    def get_service_name():
        return 'Pushbullet'

    def __init__(self, api_key, device_identifier):
        super().__init__(device_identifier)
        self._api_key = api_key
        self._notification_service = Pushbullet(self._api_key)
        self._device = self.get_device()

    def get_device(self):
        all_possible_devices = self._notification_service.devices
        for device in all_possible_devices:
            if device.nickname == self.device_identifier:
                logging.info('Found Pushbullet device: "%s"', device.nickname)
                return device
        logging.error('Did not found Pushbullet device! '
                      'These are all possible devices: "%s" '
                      'This is the device name specified in config: "%s"',
                      all_possible_devices,
                      self.device_identifier)
        return None

    def send_test_notification(self):
        self._notification_service.push_note('Test', 'Test', device=self._device)

    def send_notification(self, title, message):
        self._notification_service.push_note(title, message, device=self._device)
