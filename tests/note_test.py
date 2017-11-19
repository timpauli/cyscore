import unittest

from cyscore import Note

from .cyscore_test import CyscoreTest


class NoteTest(CyscoreTest):

    def test_repr(self):
        result = str(self.note_dummy)
        self.assertEqual(result, self.note_correct)

    def test_init_del(self):
        with self.assertRaises(AssertionError):
            Note(-1, 1, [])

    def test_init_dur(self):
        with self.assertRaises(AssertionError):
            Note(1, 0, [])

    def test_stretch(self):
        result = self.note_dummy.stretch(2)
        self.assertEqual(result.duration, 2)
        self.assertEqual(result.delay, 2)


if __name__ == '__main__':

    unittest.main()
