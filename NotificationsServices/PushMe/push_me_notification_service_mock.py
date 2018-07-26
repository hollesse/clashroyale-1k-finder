from NotificationsServices.notification_service_mock import NotificationServiceMock


class PushMeNotificationServiceMock(NotificationServiceMock):

    @staticmethod
    def get_service_name() -> str:
        return 'PushMe'
