import os
import pickle
import logging


class NotifiedGamesList:

    def __init__(self, savefile_name):
        self._savefile = os.path.join(os.path.dirname(__file__), savefile_name)
        self._notified_games_list = self.__deserialize()

    def clean(self, tournaments):
        tag_list = []
        for tournament in tournaments:
            tag_list.append(tournament['tag'])

        counter = 0
        for tag in self._notified_games_list:
            if tag not in tag_list:
                self._notified_games_list.remove(tag)
                counter += 1
        if counter > 0:
            logging.info('Removed %s tags from notified games list!', counter)

    def serialize(self):
        with open(self._savefile, 'wb') as file:
            pickle.dump(self._notified_games_list, file)
            logging.info('Saved already notified games to "%s"', self._savefile)

    def __deserialize(self):
        try:
            with open(self._savefile, 'rb') as file:
                notified_games_list = pickle.load(file)
                logging.info('Imported already notified games from "%s"', self._savefile)
                logging.debug('List of notified games: "%s"', self._notified_games_list)
                return notified_games_list
        except FileNotFoundError:
            self._notified_games_list = []
            logging.info('File for import of already notified games not found! '
                         'Expected file: "%s"', self._savefile)
            exit(1)

    def append(self, tag):
        self._notified_games_list.append(tag)

    def get(self):
        return self._notified_games_list
