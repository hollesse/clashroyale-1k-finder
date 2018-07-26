from NotificationsServices.notification_service_mock import NotificationServiceMock


class PushoverNotificationServiceMock(NotificationServiceMock):

    @staticmethod
    def get_service_name() -> str:
        return 'Pushover'
