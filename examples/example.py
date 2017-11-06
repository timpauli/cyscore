from cyscore.voice import Voice
from cyscore.score import Score
from cyscore.note import Note

from random import sample


def gen(max_amp):
    dist_pool = {0, 1, 2}
    dur_pool = {0.5, 1, 2}
    amp_pool = {0.25, 0.5, 1}
    pitch_pool = {50, 100, 150, 200, 250, 300}

    dist = sample(dist_pool, 1)[0]
    if dist == 0:
        amp_pool = set(map(lambda x: x * max_amp, amp_pool))
    dur = sample(dur_pool, 1)[0]
    amp = sample(amp_pool, 1)
    pitch = sample(pitch_pool, 1)

    return Note(dist, dur, amp + pitch)


n = 10

notes = []
max_amp = 1
for i in range(n):
    note = gen(max_amp)
    max_amp = 1 - note.pfields[0]
    notes.append(note)

voice = Voice('example', notes)
score = Score([voice])
score.render('examples/example.orc', 'examples/example')
