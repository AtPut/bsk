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

    def test_first_frame_first_throw_is_1_(self):
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
        self.assertEqual(1, bowling_game.get_frame_at(0).get_first_throw())

    def test_score_of_game_is_81(self):
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
        self.assertEqual(81, bowling_game.calculate_score())
