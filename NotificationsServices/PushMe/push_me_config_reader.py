from NotificationsServices.config_reader import ConfigReader
from NotificationsServices.PushMe.push_me_notification_service import PushMeNotificationservice


class PushMeConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushMeNotificationservice.get_service_name()

    @staticmethod
    def get_options():
        return ['device_identifier']

    def __init__(self, config):
        super().__init__(config)
