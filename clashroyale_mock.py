class ClashRoyaleMock:

    @staticmethod
    def __get_tournament(name: str, tag: str, open_game: bool, status: str, current_players: int, max_players: int):
        return {'name': name,
                'tag': tag,
                'open': open_game,
                'status': status,
                'currentPlayers': current_players,
                'maxPlayers': max_players}

    def get_open_tournaments(self):
        tournament_list = [self.__get_tournament('Mock_Tournament_valid', '1', True, 'inPreparation', 22, 25),
                           self.__get_tournament('Mock_Tournament_full', '2', True, 'inPreparation', 25, 25),
                           self.__get_tournament('Mock_Tournament_closed', '3', False, 'inPreparation', 22, 25),
                           self.__get_tournament('Mock_Tournament_ended', '4', True, 'ended', 22, 25)]
        return tournament_list

    def get_1k_tournaments(self):
        return self.get_open_tournaments()
