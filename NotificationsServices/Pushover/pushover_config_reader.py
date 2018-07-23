from NotificationsServices.config_reader import ConfigReader
from NotificationsServices.Pushover.pushover_notification_service import PushoverNotificationservice


class PushoverConfigReader(ConfigReader):

    @staticmethod
    def get_notification_service_name():
        return PushoverNotificationservice.get_service_name()

    @staticmethod
    def get_options():
        return ['api_key',
                'device_identifier']

    def __init__(self, config):
        super().__init__(config)
