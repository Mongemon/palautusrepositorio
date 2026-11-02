from player_reader import PlayerReader
from sort_by import SortBy



class StatisticsService:
    def __init__(self, playereader=PlayerReader):
        reader = playereader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, by_what):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        def sort_by_points(player):
            return player.points

        def sort_by_goals(player):
            return player.goals

        def sort_by_assists(player):
            return player.assists

        if by_what == SortBy.POINTS:
            key = sort_by_points
        elif by_what == SortBy.GOALS:
            key = sort_by_goals
        elif by_what == SortBy.ASSISTS:
            key = sort_by_assists
        else:
            return []

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=key
        )

        return sorted_players[:how_many]
