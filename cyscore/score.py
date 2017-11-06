from subprocess import call
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

    def to_file(self, fname: str) -> str:
        filename = fname + '.sco'
        with open(filename, "w") as f:
            f.write(str(self))
        return filename

    def render(self, orcname: str, fname: str,
               sr: int = 48000, ksmps: int = 1) -> None:
        call(["csound",
              "--sample-rate=" + str(sr),
              "--control-rate=" + str(sr / ksmps),
              "--logfile=" + fname + ".log",
              "--format=wav",
              "--output=" + fname + ".wav",
              "--format=24bit",
              "--nodisplays",
              orcname,
             self.to_file(fname)])
