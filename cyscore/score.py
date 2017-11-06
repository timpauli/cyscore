from voice import Voice
from typing import List


class Score:
    def __init__(self, voices: List[Voice]) -> None:
        self.voices = voices

    def __repr__(self) -> str:
        sco = ""
        for v in voices:
            block += self.__line__(time, n)
            sco += '\n'
        return block
