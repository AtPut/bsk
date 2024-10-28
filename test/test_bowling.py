import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_something(self):
        pass
    def test_define_that_game_has_10_frames(self):
        bowling_game = BowlingGame()
        bowling_game.add_frame(Frame(1, 5))
        bowling_game.add_frame(Frame(3, 6))
        bowling_game.add_frame(Frame(7, 2))
        bowling_game.add_frame(Frame(3, 6))
        bowling_game.add_frame(Frame(4, 4))
        bowling_game.add_frame(Frame(5, 3))
        bowling_game.add_frame(Frame(3, 3))
        bowling_game.add_frame(Frame(4, 5))
        bowling_game.add_frame(Frame(8, 1))
        bowling_game.add_frame(Frame(2, 6))
        self.assertEqual(10, len(bowling_game.game))

