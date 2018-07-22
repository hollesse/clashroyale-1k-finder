import configparser as configparser
import logging

from Device import Device
from PushMeConfigReader import PushMeConfigReader
from PushbulletConfigReader import PushbulletConfigReader
from PushoverConfigReader import PushoverConfigReader


class Config:

    def __init__(self, configfile_name):
        self._configfile_name = configfile_name
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
        count_devices = 0
        while True:
            try:
                notification_service_name = self._config.get('Devices', 'notification_service_' + str(count_devices+1))
                logging.debug('Reading notification service name: "%s" from config "%s"',
                              notification_service_name,
                              'notification_service_' + str(count_devices+1))
            except configparser.NoOptionError:
                break
            config_reader = self.get_config_reader(notification_service_name)
            self._device_list.append(config_reader.get_device(count_devices+1))
            count_devices += 1
        logging.info('%s devices found!', count_devices)

    def device_list(self):
        return self._device_list

    def get_config_reader(self, notification_service_name):
        return {"Pushbullet": PushbulletConfigReader(self._config),
                "Pushover": PushoverConfigReader(self._config),
                "PushMe": PushMeConfigReader(self._config)
                }.get(notification_service_name)
