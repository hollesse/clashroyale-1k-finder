from NotificationsServices.config_reader import ConfigReader
from NotificationsServices.Pushbullet.pushbullet_notification_service import PushbulletNotificationService


class PushbulletConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushbulletNotificationService.get_service_name()

    @staticmethod
    def get_options():
        return ['api_key',
                'device_identifier']

    def __init__(self, config, use_notification_service_mock):
        super().__init__(config, use_notification_service_mock)
