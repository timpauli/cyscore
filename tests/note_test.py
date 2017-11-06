import unittest

from cyscore.note import Note


class NoteTest(unittest.TestCase):

    def test_repr(self):
        dummy = Note(1, [2, 3])
        result = str(dummy)
        correct = '1\t2\t3'
        self.assertEqual(result, correct)


if __name__ == '__main__':

    unittest.main()
