import configparser
import logging

from device import Device


class ConfigReader:
    """Abstract Class which should be used to implement the reading
    of the config for different notification services"""

    def __init__(self, config):
        self._config = config

    def get_device(self, device_number):
        options_dict = self.read_config(device_number, self.get_options())
        logging.debug('Try to get device for %s with following options: %s',
                      self.get_notification_service_name(),
                      options_dict)
        return Device(self.get_notification_service_name(), options_dict)

    def read_config(self, device_number, options):
        options_dict = {}
        for key in options:
            try:
                options_dict[key] = self._config.get('Device_' + str(device_number), key)
                ConfigReader.log_read_option(key, options_dict[key], device_number)
            except configparser.NoOptionError:
                ConfigReader.log_no_option_error(key, device_number)
                exit(1)
        return options_dict

    @staticmethod
    def get_options() -> list:
        """
        Returns a list of optionnames which should be specified in
        the configfile for a device that uses this service.
        :return: list of optionnames
        """
        raise NotImplementedError("Should have implemented this")

    @staticmethod
    def get_notification_service_name() -> str:
        """
        Returns the notification service name the config reader
        belongs to. Therefore the static method
        get_notification_service_name() of the notification service
        should be used
        :return: Name of the notification service the config reader
        belongs to as a string
        """
        raise NotImplementedError("Should have implemented this")

    @staticmethod
    def log_no_option_error(option, device_number):
        logging.error('Option "%s" missing in configuration for "%s"',
                      option,
                      'Device_' + str(device_number))

    @staticmethod
    def log_read_option(key, option, device_number):
        logging.debug('Reading %s: "%s" from config "%s"',
                      key,
                      option,
                      'Device_' + str(device_number))
