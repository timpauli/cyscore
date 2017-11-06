from typing import List

from .voice import Voice


class Score:
    def __init__(self, voices: List[Voice]) -> None:
        assert(len(voices) > 0)
        self.voices = voices

    def __repr__(self) -> str:
        sco = str(self.voices[0])
        for v in self.voices[1:]:
            sco += '\n'
            sco += str(v)
        return sco
