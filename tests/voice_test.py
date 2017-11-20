import unittest

from cyscore import Voice

from .cyscore_test import CyscoreTest


class VoiceTest(CyscoreTest):

    def test_repr(self):
        result = str(self.voice_dummy)
        self.assertEqual(result, self.voice_correct)

    def test_init_len(self):
        with self.assertRaises(AssertionError):
            Voice('test', [])

    def test_iter(self):
        result = Voice(self.voice_dummy.instr, list(map(
            lambda x: x.stretch(1), self.voice_dummy)))
        self.assertEqual(result, self.voice_dummy)

    def test_get_item(self):
        result = self.voice_dummy[0]
        self.assertEqual(result, self.note_dummy)


if __name__ == '__main__':

    unittest.main()
