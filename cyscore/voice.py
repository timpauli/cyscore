from typing import List

import numpy as np

from note import Note, Rest


class Voice:
    def __init__(self, instr: str, notes: List[Note]) -> None:
        self instr = instr
        self.notes = notes

    def __line__(self, time: float, note: Note) -> str:
        line = "i\t{0}\t{1}\t".format(self.instr, time)
        return line + str(note)

    def __repr__(self) -> str:
        durs = map(lambda x: x.dur, self.notes)
        block = self.__line__(time, self.notes[0])
        for n, time in zip(self.notes[1:], np.cumsum(durs)):
            if n is not Rest:
                block += '\n'
                block += self.__line__(time, n)
        return block
