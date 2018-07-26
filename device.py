import logging

from NotificationsServices.PushMe.push_me_notification_service import PushMeNotificationService
from NotificationsServices.PushMe.push_me_notification_service_mock import PushMeNotificationServiceMock
from NotificationsServices.Pushbullet.pushbullet_notification_service import PushbulletNotificationService
from NotificationsServices.Pushbullet.pushbullet_notification_service_mock import PushbulletNotificationServiceMock
from NotificationsServices.Pushover.pushover_notification_service import PushoverNotificationService
from NotificationsServices.Pushover.pushover_notification_service_mock import PushoverNotificationServiceMock


class Device:

    def __init__(self, notification_service_name, options_dict, use_notification_service_mock):
        self._notification_service = Device.new_notification_service(notification_service_name,
                                                                     options_dict,
                                                                     use_notification_service_mock)

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
    def new_notification_service(notification_service_name, options_dict, use_notification_service_mock):
        if notification_service_name == PushbulletNotificationService.get_service_name():
            if use_notification_service_mock:
                return PushbulletNotificationServiceMock(options_dict['device_identifier'])
            else:
                return PushbulletNotificationService(options_dict['api_key'],
                                                     options_dict['device_identifier'])
        if notification_service_name == PushoverNotificationService.get_service_name():
            if use_notification_service_mock:
                return PushoverNotificationServiceMock(options_dict['device_identifier'])
            else:
                return PushoverNotificationService(options_dict['api_key'],
                                                   options_dict['device_identifier'])
        if notification_service_name == PushMeNotificationService.get_service_name():
            if use_notification_service_mock:
                return PushMeNotificationServiceMock(options_dict['device_identifier'])
            else:
                return PushMeNotificationService(options_dict['device_identifier'])
        logging.error('Notification Service "%s" does not exist!',
                      notification_service_name)
        return None
