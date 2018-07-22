import configparser
import logging

from ConfigReader import ConfigReader
from Device import Device
from PushoverNotificationService import PushoverNotificationService


class PushoverConfigReader(ConfigReader):

    def __init__(self, config):
        super().__init__(config)

    def get_device(self, device_number):
        api_key = None
        try:
            api_key = self._config.get('Devices', 'api_key_' + str(device_number))
            logging.debug('Reading api key: "%s" from config "%s"',
                          api_key,
                          'api_key_' + str(device_number))
        except configparser.NoOptionError:
            logging.error('Option "%s" missing in configuration', 'api_key_' + str(device_number))
            exit(1)

        device_identifier = None
        try:
            device_identifier = self._config.get('Devices', 'device_identifier_' + str(device_number))
            logging.info('Reading device identifier: "%s from config "%s"',
                         device_identifier,
                         'device_identifier_' + str(device_number))
        except configparser.NoOptionError:
            logging.error('Option "%s" missing in configuration', 'device_identifier_' + str(device_number))
            exit(1)

        return Device(PushoverNotificationService.get_service_name(), device_identifier, api_key)