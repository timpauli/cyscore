import unittest

from cyscore import Note, Score, Voice


class CyscoreTest(unittest.TestCase):
    note_dummy = Note(1, 1, [2, 3])
    note_correct = '1\t2\t3'
    voice_dummy = Voice('test', [note_dummy] * 2)
    voice_correct_skel = 'i\t\"test\"\t{0}\t' + note_correct
    voice_correct = voice_correct_skel.format(
        0) + '\n' + voice_correct_skel.format(1)
    score_dummy = Score([voice_dummy] * 2)
    score_correct = voice_correct + '\n' + voice_correct
