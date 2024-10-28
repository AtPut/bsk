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
        i = 0
        while i < len(self.game):
            frame = self.get_frame_at(i)
            score += frame.score()
            if frame.is_spare():
                 score += self.get_frame_at(i + 1).get_first_throw()
            i += 1

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
