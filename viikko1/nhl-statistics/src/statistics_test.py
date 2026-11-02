import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stub = PlayerReaderStub()
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(self.stub)

    def test_search_name(self):
        name = self.stats.search("Semenko")
        self.assertEqual(name, self.stub.get_players()[0])

    def test_search_no_name(self):
        name = self.stats.search("-_-")
        self.assertEqual(name, None)

    def test_search_team(self):
        team = self.stats.team("EDM")
        self.assertEqual(set(team), {self.stub.get_players()[0], 
            self.stub.get_players()[2], 
            self.stub.get_players()[4]
            })

    def test_search_no_team(self):
        team = self.stats.team("-_-")
        self.assertEqual(team, [])

    def test_top(self):
        top_players = self.stats.top(2, SortBy.POINTS)

        self.assertEqual(top_players, [self.stub.get_players()[4], 
            self.stub.get_players()[1]
            ])

    def test_top_zero(self):
        top_players = self.stats.top(0, SortBy.POINTS)
        self.assertEqual(top_players, [])

    def test_top_others(self):
        top_players = self.stats.top(1, SortBy.GOALS)
        self.assertEqual(top_players, [self.stub.get_players()[1]])

        top_players = self.stats.top(1, SortBy.ASSISTS)
        self.assertEqual(top_players, [self.stub.get_players()[4]])

        top_players = self.stats.top(1, "bruh")
        self.assertEqual(top_players, [])



