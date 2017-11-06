from random import sample

from cyscore.note import Note
from cyscore.score import Score
from cyscore.voice import Voice


def gen(max_amp, prev_dur):
    dist_pool = {0, 1, 2}
    dur_pool = {0.5, 1, 2}
    amp_pool = {0.25, 0.5, 1}
    pitch_pool = {50, 100, 150, 200, 250, 300}

    new_max = 1
    dist = sample(dist_pool, 1)[0]
    cond = dist < prev_dur
    if cond:
        amp_pool = set(map(lambda x: x * max_amp, amp_pool))
    dur = sample(dur_pool, 1)[0]
    amp = sample(amp_pool, 1)
    pitch = sample(pitch_pool, 1)

    if cond:
        new_max = max_amp - amp[0]
    return Note(dist, dur, amp + pitch), new_max


n = 10

notes = []
max_amp = 1
prev_dur = 0
for i in range(n):
    note, max_amp = gen(max_amp, prev_dur)
    prev_dur = note.duration
    notes.append(note)

voice = Voice('example', notes)
score = Score([voice])
score.render('examples/example.orc', 'examples/example')
