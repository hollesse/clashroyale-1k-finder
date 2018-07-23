import logging

from NotificationsServices.PushMe.push_me_notification_service import PushMeNotificationservice
from NotificationsServices.Pushbullet.pushbullet_notification_service import PushbulletNotificationservice
from NotificationsServices.Pushover.pushover_notification_service import PushoverNotificationservice


class Device:

    def __init__(self, notification_service_name, options_dict):
        self._notification_service = Device.new_notification_service(notification_service_name,
                                                                     options_dict)

    def send_notification(self, tournament):
        self._notification_service.send_notification('1K Tournament found!',
                                                     'Name: ' + tournament['name'])
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
            return PushbulletNotificationservice(options_dict['api_key'],
                                                 options_dict['device_identifier'])
        if notification_service_name == 'Pushover':
            return PushoverNotificationservice(options_dict['api_key'],
                                               options_dict['device_identifier'])
        if notification_service_name == 'PushMe':
            return PushMeNotificationservice(options_dict['device_identifier'])
        logging.error('Notification Service "%s" does not exist!',
                      notification_service_name)
        return None
