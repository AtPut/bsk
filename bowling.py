from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.game = []
    
    def add_frame(self, frame: Frame) -> None:
        self.game.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i < len(self.game):
            return self.game[i]
        raise BowlingError

    def calculate_score(self) -> int:
        score = 0
        i = 0
        while i < len(self.game):
            frame = self.get_frame_at(i)
            if frame.is_strike():
                score += self.get_frame_at(i + 1).score()
                if self.get_frame_at(i + 1).is_strike():
                    score += self.get_frame_at(i + 2).get_first_throw()
            elif frame.is_spare():
                if i is not len(self.game) - 1:
                    score += self.get_frame_at(i + 1).get_first_throw()
            score += frame.score()
            i += 1

        return score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        if self.get_frame_at(-1).is_spare():
            self.game[-1].set_bonus(bonus_throw)
        else:
            raise BowlingError

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
