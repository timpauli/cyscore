from typing import List


class Note:
    def __init__(self, dur: float, pfields: List[float]) -> None:
        self.dur = dur
        self.pfields = pfields

    def __repr__(self) -> str:
        line = str(self.dur)
        for p in self.pfields:
            line += '\t'
            line += str(p)
        return line


class Rest(Note):
    def __init__(self, dur: float) -> None:
        Note.__init__(dur, [])
