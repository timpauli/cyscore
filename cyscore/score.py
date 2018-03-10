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

    def repr(self, mutefuncs) -> str:
        sco = self.voices[0].repr(mutefuncs[0])
        for v, m in zip(self.voices[1:], mutefuncs[1:]):
            sco += '\n'
            sco += v.repr(m)
        return sco

    def __repr__(self) -> str:
        return self.repr([lambda x: True] * len(self.voices))

    def to_file(self, fname: str, mutefuncs=None) -> str:
        if mutefuncs is None:
            mutefuncs = [lambda x: True] * len(self.voices)
        with open(fname, "w") as f:
            f.write(self.repr(mutefuncs))
        return fname

    def render(self, orcname: str, sconame: str, outname: str,
               sr: int=48000, ksmps: int=1, depth: str='float',
               logname: str="", mutefuncs=None) -> str:
        if mutefuncs is None:
            mutefuncs = [lambda x: True] * len(self.voices)
        sconame = self.to_file(sconame, mutefuncs)
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
