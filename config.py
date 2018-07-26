import configparser
import logging

from NotificationsServices.PushMe.push_me_config_reader import PushMeConfigReader
from NotificationsServices.Pushbullet.pushbullet_config_reader import PushbulletConfigReader
from NotificationsServices.Pushover.pushover_config_reader import PushoverConfigReader


class Config:

    def __init__(self, configfile_name, use_notification_service_mock):
        self._configfile_name = configfile_name
        self._use_notification_service_mock = use_notification_service_mock
        self._config = configparser.ConfigParser()
        self._config.read(self._configfile_name)
        logging.info('Reading config file "%s"', self._configfile_name)
        self._clashroyale_api_key = None
        self.__read_clashroyale_api_key()
        self._device_list = []
        self.__read_device_list()

    def clashroyale_api_key(self):
        return self._clashroyale_api_key

    def __read_clashroyale_api_key(self):
        self._clashroyale_api_key = self._config.get('ClashRoyale', 'clashroyale_api_key')
        logging.debug('Reading ClashRoyale api key: "%s"', self._clashroyale_api_key)

    def __read_device_list(self):
        device_number = 0
        while True:
            device_number += 1
            try:
                notification_service_name = self._config.get('Device_' + str(device_number),
                                                             'notification_service')
                logging.debug('Reading notification service name: "%s" from config "%s"',
                              notification_service_name,
                              'Device_' + str(device_number))
            except configparser.NoSectionError:
                break
            config_reader = self.get_config_reader(notification_service_name)
            self._device_list.append(config_reader.get_device(device_number))

        logging.info('%s devices found!', device_number - 1)

    def device_list(self):
        return self._device_list

    def get_config_reader(self, notification_service_name):
        return {"Pushbullet": PushbulletConfigReader(self._config, self._use_notification_service_mock),
                "Pushover": PushoverConfigReader(self._config, self._use_notification_service_mock),
                "PushMe": PushMeConfigReader(self._config, self._use_notification_service_mock)
                }.get(notification_service_name)
