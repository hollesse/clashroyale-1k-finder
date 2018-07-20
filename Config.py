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
                pushbullet_api_key = self._config.get('Devices', 'pushbullet_api_key_' + str(count_devices+1))
                logging.debug('Reading Pushbullet api key: "%s"', pushbullet_api_key)
            except configparser.NoOptionError:
                break

            try:
                pushbullet_device_name = self._config.get('Devices', 'pushbullet_device_name_' + str(count_devices+1))
                logging.info('Reading Pushbullet device name: "%s', pushbullet_device_name)
            except configparser.NoOptionError:
                break

            self._device_list.append(Device(pushbullet_api_key, pushbullet_device_name))
            count_devices += 1
        logging.info('%s devices found!', count_devices)

    def device_list(self):
        return self._device_list
