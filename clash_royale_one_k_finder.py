import logging
import clashroyale

from clashroyale_mock import ClashRoyaleMock
from config import Config
from notified_games_list import NotifiedGamesList


class ClashRoyaleOneKFinder:

    def __init__(self,
                 configfile_name,
                 debug=False,
                 disable_cache=False,
                 use_clashroyale_mock=False,
                 use_notification_service_mock=False):
        if debug:
            logging.basicConfig(level=logging.DEBUG,
                                format='%(levelname)s: %(asctime)s: %(message)s')
        else:
            logging.basicConfig(level=logging.INFO,
                                format='%(levelname)s: %(asctime)s: %(message)s')
        logging.info('##### Started ClashRoyalOneKFinder #####')
        self._debug = debug
        self._disable_cache = disable_cache
        self._config = Config(configfile_name, use_notification_service_mock)
        if use_clashroyale_mock:
            self._clashroyale = ClashRoyaleMock()
        else:
            self._clashroyale = clashroyale.RoyaleAPI(self._config.clashroyale_api_key())
        self._device_list = self._config.device_list()
        self._notified_games = NotifiedGamesList('notified-games.pkl', disable_cache=disable_cache)

    def find_open_1k_tournaments(self):
        if self._debug:
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
