import logging

from NotificationsServices.PushMe.PushMeNotificationService import PushMeNotificationService
from NotificationsServices.Pushbullet.PushbulletNotificationService import PushbulletNotificationService
from NotificationsServices.Pushover.PushoverNotificationService import PushoverNotificationService


class Device:

    def __init__(self, notification_service_name, options_dict):
        self._notification_service = Device.new_notification_service(notification_service_name, options_dict)

    def send_notification(self, tournament):
        self._notification_service.send_notification('1K Tournament found!', 'Name: ' + tournament['name'])
        logging.info('Pushbullet notification sent to "%s"! Tag: "%s" Name: "%s"',
                     self._notification_service.device_identifier,
                     tournament['tag'],
                     tournament['name'])

    def test_notification(self):
        self._notification_service.send_test_notification()
        logging.info('Test notification sent to "%s" via "%s!',
                     self._notification_service.device_identifier,
                     self._notification_service.get_service_name())

    @staticmethod
    def new_notification_service(notification_service_name, options_dict):
        if notification_service_name == 'Pushbullet':
            return PushbulletNotificationService(options_dict['api_key'], options_dict['device_identifier'])
        elif notification_service_name == 'Pushover':
            return PushoverNotificationService(options_dict['api_key'], options_dict['device_identifier'])
        elif notification_service_name == 'PushMe':
            return PushMeNotificationService(options_dict['device_identifier'])
        else:
            logging.error('Notification Service "%s" does not exist!', notification_service_name)
            exit(1)



