from typing import List

from itertools import accumulate

from .note import Note, Rest


class Voice:
    def __init__(self, instr: str, notes: List[Note]) -> None:
        assert(len(notes) > 0)
        self.instr = instr
        self.notes = notes

    def __line(self, time: float, note: Note) -> str:
        line = "i\t\"{0}\"\t{1}\t".format(self.instr, time)
        return line + str(note)

    def __repr__(self) -> str:
        durs = map(lambda x: x.dur, self.notes)
        block = self.__line(0, self.notes[0])
        for n, time in zip(self.notes[1:], accumulate(durs)):
            if n is not Rest:
                block += '\n'
                block += self.__line(time, n)
        return block
