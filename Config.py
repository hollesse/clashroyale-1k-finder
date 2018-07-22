import configparser as configparser
import logging

from Device import Device


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

            try:
                api_key = self._config.get('Devices', 'api_key_' + str(count_devices+1))
                logging.debug('Reading api key: "%s" from config "%s"',
                              api_key,
                              'api_key_' + str(count_devices+1))
            except configparser.NoOptionError:
                break

            try:
                device_identifier = self._config.get('Devices', 'device_identifier_' + str(count_devices+1))
                logging.info('Reading device identifier: "%s from config "%s"',
                             device_identifier,
                             'device_identifier_' + str(count_devices + 1))
            except configparser.NoOptionError:
                break

            self._device_list.append(Device(api_key, device_identifier, str(notification_service_name)))
            count_devices += 1
        logging.info('%s devices found!', count_devices)

    def device_list(self):
        return self._device_list
