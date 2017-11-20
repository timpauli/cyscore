from typing import List


class Note:
    def __init__(self, delay: float, duration: float,
                 pfields: List) -> None:
        assert(delay >= 0)
        assert(duration > 0)
        self.__delay = delay
        self.__duration = duration
        self.__pfields = pfields

    @property
    def delay(self) -> float:
        return self.__delay

    @property
    def duration(self) -> float:
        return self.__duration

    @property
    def pfields(self) -> List:
        return list(self.__pfields)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            de = self.delay == other.delay
            du = self.duration == other.duration
            p = self.pfields == other.pfields
            return de and du and p
        else:
            return self == other

    def __repr__(self) -> str:
        line = str(self.duration)
        for p in self.pfields:
            line += '\t'
            line += str(p)
        return line

    def stretch(self, factor: float):
        assert(factor > 0)
        return self.__class__(self.delay * factor, self.duration * factor,
                              self.pfields)
