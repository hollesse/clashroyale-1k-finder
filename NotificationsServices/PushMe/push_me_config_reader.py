from NotificationsServices.config_reader import ConfigReader
from NotificationsServices.PushMe.push_me_notification_service import PushMeNotificationService


class PushMeConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushMeNotificationService.get_service_name()

    @staticmethod
    def get_options():
        return ['device_identifier']

    def __init__(self, config, use_notification_service_mock):
        super().__init__(config, use_notification_service_mock)
