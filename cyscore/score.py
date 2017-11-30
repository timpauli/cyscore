import subprocess as sp
from typing import List

from .voice import Voice


class Score:
    def __init__(self, voices: List[Voice]) -> None:
        assert(len(voices) > 0)
        self.__voices = voices

    @property
    def voices(self) -> List[Voice]:
        return list(self.__voices)

    def __repr__(self) -> str:
        sco = str(self.voices[0])
        for v in self.voices[1:]:
            sco += '\n'
            sco += str(v)
        return sco

    def to_file(self, fname: str) -> str:
        with open(fname, "w") as f:
            f.write(str(self))
        return fname

    def render(self, orcname: str, sconame: str, outname: str,
               sr: int=48000, ksmps: int=1, depth: str='24bit',
               logname: str="") -> str:
        sconame = self.to_file(sconame)
        args = ["csound",
                "--sample-rate=" + str(sr),
                "--control-rate=" + str(sr / ksmps),
                "--output=" + outname,
                "--format=wav",
                "--format=" + depth,
                "--nodisplays"]
        if logname:
            args.append("--logfile=" + logname)
        args.extend([orcname, sconame])
        sp.run(args)
        return outname
