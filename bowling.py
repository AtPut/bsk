from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.game = []
    
    def add_frame(self, frame: Frame) -> None:
        self.game.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if 0 <= i < len(self.game):
            return self.game[i]
        raise BowlingError

    def calculate_score(self) -> int:
        score = 0
        for frame in self.game:
            score += frame.score()
        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
