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


if __name__ == '__main__':

    unittest.main()
