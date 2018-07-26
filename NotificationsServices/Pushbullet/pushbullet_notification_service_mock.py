from NotificationsServices.notification_service_mock import NotificationServiceMock


class PushbulletNotificationServiceMock(NotificationServiceMock):

    @staticmethod
    def get_service_name() -> str:
        return 'Pushbullet'
