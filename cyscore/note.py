from typing import List


class Note:
    def __init__(self, distance: float, duration: float,
                 pfields: List[float]) -> None:
        self.distance = distance
        self.duration = duration
        self.pfields = pfields

    def __repr__(self) -> str:
        line = str(self.duration)
        for p in self.pfields:
            line += '\t'
            line += str(p)
        return line
