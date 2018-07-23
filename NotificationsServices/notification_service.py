class NotificationService:
    """Abstract Class which should be used to implement different notification services"""

    def __init__(self, device_identifier):
        self.device_identifier = device_identifier

    def send_notification(self, title: str, message: str) -> None:
        """
        Sends a notification to inform about newly found 1k tournaments to the device
        with the device_identifier created in the constructor. Some notification services
        also need an api key.
        :param title: The title of the notification
        :param message: The message contained in the notification
        """
        raise NotImplementedError("Should have implemented this")

    def send_test_notification(self) -> None:
        """
        Sends a test notification to the device with the device_identifier created in the
        constructor.
        This notifications title is "Test" and also the message is "Test"
        Some notification services also need an api key.
        """
        raise NotImplementedError("Should have implemented this")

    @staticmethod
    def get_service_name() -> str:
        """
        This method returns the service name as a string.
        :return: Name of the service which is implemented
        """
        raise NotImplementedError("Should have implemented this")
