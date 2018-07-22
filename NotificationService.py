class NotificationService(object):
    """Abstract Class which should be used to implement different notification services"""

    def __init__(self, api_key, device_identifier):
        self._api_key = api_key
        self.device_identifier = device_identifier

    def send_notification(self, title, message):
        raise NotImplementedError("Should have implemented this")

    def send_test_notification(self):
        raise NotImplementedError("Should have implemented this")

    def get_service_name(self):
        raise NotImplementedError("Should have implemented this")



