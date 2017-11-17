from typing import List


class Note:
    def __init__(self, delay: float, duration: float,
                 pfields: List) -> None:
        assert(delay >= 0)
        assert(duration > 0)
        self.delay = delay
        self.duration = duration
        self.pfields = pfields

    def __repr__(self) -> str:
        line = str(self.duration)
        for p in self.pfields:
            line += '\t'
            line += str(p)
        return line

    def stretch(self, factor):
        return Note(self.delay * factor, self.duration * factor, self.pfields)
