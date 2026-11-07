import requests

class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = int(dict['goals'])
        self.assists = int(dict['assists'])
    
    def __str__(self):
        return (
                f"{self.name:20}{self.nationality:5}"
                f"{self.team:15}{self.goals:2} + "
                f"{self.assists:2} = {self.goals + self.assists}"
                )


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        top_players = []

        for player in self.players:
            if player.nationality == nationality:
                top_players.append(player)

        top_players.sort(key=lambda x: int(x.assists)+int(x.goals), reverse=True)

        return top_players
