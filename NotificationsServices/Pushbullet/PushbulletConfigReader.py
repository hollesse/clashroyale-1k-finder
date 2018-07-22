from ConfigReader import ConfigReader
from PushbulletNotificationService import PushbulletNotificationService


class PushbulletConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushbulletNotificationService.get_service_name()

    @staticmethod
    def get_options():
        return ['api_key',
                'device_identifier']

    def __init__(self, config):
        super().__init__(config)
