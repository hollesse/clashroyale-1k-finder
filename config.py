import configparser
import logging
import os.path
import config_options

from NotificationsServices.PushMe.push_me_config_reader import PushMeConfigReader
from NotificationsServices.Pushbullet.pushbullet_config_reader import PushbulletConfigReader
from NotificationsServices.Pushover.pushover_config_reader import PushoverConfigReader


class Config:

    def __init__(self, configfile_name):
        self._configfile_name = configfile_name
        self._config = configparser.ConfigParser()
        self.__read_configfile()
        self._device_options_dict_list = self.__read_device_options_dict_list()
        self._clashroyale_options_dict = self.__read_options(config_options.clashroyale_section_name(),
                                                             config_options.clashroyale_option_list())
        self._developer_options_dict = self.__read_options(config_options.developer_section_name(),
                                                           config_options.developer_option_list(),
                                                           True,
                                                           True,
                                                           config_options.developer_default_option_dict())

    def __read_options(self, section_name: str, option_name_list: list, option_is_bool_value: bool = False,
                       no_error_logging: bool = False, default_dict: dict = {}) -> dict:
        result_dict = default_dict
        for option in option_name_list:
            value = self.__read_option(section_name, option, option_is_bool_value, no_error_logging)
            if value is not None:
                result_dict[option] = value
        return result_dict

    def __read_option(self, section_name: str, option_name: str, option_is_bool_value: bool =False,
                      no_error_logging: bool = False):
        try:
            if option_is_bool_value:
                result = self._config.getboolean(section_name, option_name)
            else:
                result = self._config.get(section_name, option_name)
            logging.debug('Reading %s %s: "%s"', section_name, option_name, result)
            return result
        except configparser.NoSectionError:
            if not no_error_logging:
                logging.error('Did not found section "%s" in configfile "%s"', section_name, self._configfile_name)
            return None
        except configparser.NoOptionError:
            if not no_error_logging:
                logging.error('Did not found option "%s" in section "%s" in configfile "%s"', option_name, section_name, self._configfile_name)
            return None

    def __read_device_options_dict_list(self) -> list:
        device_options_dict_list = []
        while True:
            device_number = len(device_options_dict_list) + 1
            section_name = 'Device_' + str(device_number)
            notification_service_name = self.__read_option(section_name, 'notification_service', no_error_logging=True)
            if notification_service_name is not None:
                logging.debug('Reading notification service name: "%s" from config "%s"',
                              notification_service_name,
                              section_name)
                notification_service_config_reader = self.get_config_reader(notification_service_name)
                device_options = notification_service_config_reader.get_options_dict(device_number)
                device_options_dict_list.append({'notification_service_name': notification_service_name,
                                                 'device_options': device_options})
            else:
                break
        logging.info('%s devices found!', len(device_options_dict_list))
        return device_options_dict_list

    def get_config_reader(self, notification_service_name):
        return {PushbulletConfigReader.get_notification_service_name():
                    PushbulletConfigReader(self._config),
                PushoverConfigReader.get_notification_service_name():
                    PushoverConfigReader(self._config),
                PushMeConfigReader.get_notification_service_name():
                    PushMeConfigReader(self._config)
                }.get(notification_service_name)

    def __read_configfile(self):
        file_path = os.path.join(os.path.dirname(__file__), self._configfile_name)
        if os.path.isfile(self._configfile_name):
            self._config.read(self._configfile_name)
            logging.info('Reading config file "%s"', self._configfile_name)
        else:
            logging.error('Config file "%s" does not exist!', file_path)
            raise FileNotFoundError

    def get_clashroyale_options_dict(self):
        return self._clashroyale_options_dict

    def get_developer_options_dict(self):
        return self._developer_options_dict

    def get_device_options_dict_list(self):
        return self._device_options_dict_list

    @staticmethod
    def is_debug_mode(configfile_name: str) -> bool:
        config = configparser.ConfigParser()
        if os.path.isfile(configfile_name):
            config.read(configfile_name)
        else:
            raise FileNotFoundError
        try:
            is_debug = config.getboolean(config_options.developer_section_name(), 'debug')
            return is_debug
        except configparser.NoSectionError:
            return False
        except configparser.NoOptionError:
            return False
