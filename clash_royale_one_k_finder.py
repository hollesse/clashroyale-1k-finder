import logging
import clashroyale

import config

from clashroyale_mock import ClashRoyaleMock
from device import Device
from notified_games_list import NotifiedGamesList


class ClashRoyaleOneKFinder:

    def __init__(self, configfile_name):
        if config.Config.is_debug_mode(configfile_name):
            logging.basicConfig(level=logging.DEBUG,
                                format='%(levelname)s: %(asctime)s: %(message)s')
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(levelname)s: %(asctime)s: %(message)s')
        self._config = config.Config(configfile_name)
        self._clashroyale_options_dict = self._config.get_clashroyale_options_dict()
        self._developer_options_dict = self._config.get_developer_options_dict()
        self._device_options_dict_list = self._config.get_device_options_dict_list()
        if self._developer_options_dict['mock_clashroyale']:
            self._clashroyale = ClashRoyaleMock()
        else:
            self._clashroyale = clashroyale.RoyaleAPI(self._config.get_clashroyale_options_dict()['clashroyale_api_key'])
        self._device_list = self.__get_device_list()
        self._notified_games = NotifiedGamesList('notified-games.pkl',
                                                 disable_cache=self._developer_options_dict['disable_cache'])

    def find_open_1k_tournaments(self) -> None:
        if self._developer_options_dict['debug']:
            one_k_tournaments = self._clashroyale.get_open_tournaments()
        else:
            one_k_tournaments = self._clashroyale.get_1k_tournaments()
        for tournament in one_k_tournaments:
            if tournament['open'] \
                    and tournament['maxPlayers'] > tournament['currentPlayers'] \
                    and tournament['status'] == 'inPreparation':
                if tournament['tag'] not in self._notified_games.get():
                    for device in self._device_list:
                        device.send_notification(tournament)
                else:
                    logging.info('Notification already sent! Tag: "%s" Name: "%s"',
                                 tournament['tag'],
                                 tournament['name'])
                if tournament['tag'] not in self._notified_games.get():
                    self._notified_games.append(tournament['tag'])
                    logging.debug('Added Tag "%s" to notified games list', tournament['tag'])
        self._notified_games.clean(one_k_tournaments)
        self._notified_games.serialize()

    def __get_device_list(self) -> list:
        device_list = []
        for device_option_dict in self._device_options_dict_list:
            device = Device(device_option_dict['notification_service_name'],
                            device_option_dict['device_options'],
                            self._developer_options_dict['mock_notification_services'])
            device_list.append(device)
        return device_list
