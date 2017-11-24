from typing import List, Union

Parameter = Union[Union[int, float], str]


class Note:
    def __init__(self, delay: float, duration: float,
                 pfields: List[Parameter]) -> None:
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
    def pfields(self) -> List[Parameter]:
        return list(self.__pfields)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.__eq(other)
        else:
            return False

    def __eq(self, other: 'Note') -> bool:
        de = self.delay == other.delay
        du = self.duration == other.duration
        p = self.pfields == other.pfields
        return de and du and p

    def __repr__(self) -> str:
        line = str(self.duration)
        for p in self.pfields:
            line += '\t'
            line += str(p)
        return line

    def stretch(self, factor: float) -> 'Note':
        assert(factor > 0)
        return type(self)(self.delay * factor, self.duration * factor,
                          self.pfields)

    def change_del(self, delay: float) -> 'Note':
        assert(delay >= 0)
        return type(self)(delay, self.duration,
                          self.pfields)

    def change_dur(self, duration: float) -> 'Note':
        assert(duration > 0)
        return type(self)(self.delay, duration,
                          self.pfields)
