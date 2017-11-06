sr = 48000
ksmps = 1
nchnls = 2
0dbfs = 1

instr example
  ;clarifying arguments (p-fields)
  iDuration = p3
  iAmp = p4
  iPitch = p5
  ; envelope
  kEnv line iAmp, iDuration, 0
  ; synthesis
  aSig pluck kEnv, iPitch, iPitch, 0, 1
  outs aSig, aSig
endin
