from itertools import accumulate
from typing import Iterator, List

from .note import Note


class Voice:
    def __init__(self, instr: str, notes: List[Note]) -> None:
        assert(len(notes) > 0)
        self.__instr = instr
        self.__notes = notes

    @property
    def instr(self) -> str:
        return self.__instr

    @property
    def notes(self) -> List[Note]:
        return list(self.__notes)

    def __iter__(self) -> Iterator[Note]:
        return self.notes.__iter__()

    def __getitem__(self, index: int) -> Note:
        return self.notes[index]

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.__eq(other)
        else:
            False

    def __eq(self, other: 'Voice') -> bool:
        i = self.instr == other.instr
        n = self.notes == other.notes
        return i and n

    def __line(self, time: float, note: Note) -> str:
        line = "i\t\"{0}\"\t{1}\t".format(self.instr, time)
        return line + str(note)

    def __repr__(self) -> str:
        times = accumulate(map(lambda x: x.delay, self.notes))
        block = self.__line(0, self.notes[0])
        for n, time in zip(self.notes[1:], times):
            block += '\n'
            block += self.__line(time, n)
        return block
