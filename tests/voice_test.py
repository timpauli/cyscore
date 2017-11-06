import unittest

from cyscore.voice import Voice

# TODO
class VoiceTest(unittest.TestCase):

    def test_repr(self):
        dummy = Voice('hello', [2, 3])
        result = str(dummy)
        correct = '1\t2\t3'
        self.assertEqual(result, correct)


if __name__ == '__main__':

    unittest.main()
