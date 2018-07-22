from NotificationsServices.ConfigReader import ConfigReader
from NotificationsServices.PushMe.PushMeNotificationService import PushMeNotificationService


class PushMeConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushMeNotificationService.get_service_name()

    @staticmethod
    def get_options():
        return ['device_identifier']

    def __init__(self, config):
        super().__init__(config)
