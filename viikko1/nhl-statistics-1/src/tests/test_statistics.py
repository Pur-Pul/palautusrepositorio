import unittest
from player import Player
from statistics import Statistics
from sort_by import SortBy

class PlayerReaderStub:
    def __init__(self):
        self.players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
            ]
    def get_players(self):
        return self.players
class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.statistics = Statistics(self.reader)
        self.players = self.reader.get_players()

    def test_search_finds_player(self):
        name = "Semenko"
        self.assertEqual(self.players[0], self.statistics.search(name))
    
    def test_search_finds_player_by_partial_name(self):
        name = "Semenko"
        self.assertEqual(self.players[0], self.statistics.search(name[:3]))
    
    def test_search_returns_None_if_player_not_found(self):
        self.assertEqual(None, self.statistics.search("Rolf"))
    
    def test_team_returns_list_of_players_int_team(self):
        self.assertEqual(
            [self.players[0], self.players[2], self.players[4]],
            self.statistics.team("EDM")
        )
    
    def test_top_returns_a_list_of_specified_length(self):
        self.assertEqual(4, len(self.statistics.top(3)))

    def test_top_returns_list_of_players_in_order_of_points(self):
        self.assertEqual(
            [self.players[4], self.players[1], self.players[3], self.players[2], self.players[0]],
            self.statistics.top(4)
        )
    
    def test_top_returns_list_of_players_in_order_of_goals(self):
        self.assertEqual(
            [self.players[1], self.players[3], self.players[2], self.players[4], self.players[0]],
            self.statistics.top(4, SortBy.GOALS)
        )
    
    def test_top_returns_list_of_players_in_order_of_assists(self):
        self.assertEqual(
            [self.players[4], self.players[3], self.players[1], self.players[2], self.players[0]],
            self.statistics.top(4, SortBy.ASSISTS)
        )
