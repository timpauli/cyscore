import unittest

from cyscore import Score

from cyscore_test import CyscoreTest


class ScoreTest(CyscoreTest):

    def test_repr(self):
        result = str(self.score_dummy)
        self.assertEqual(result, self.score_correct)

    def test_init_len(self):
        with self.assertRaises(AssertionError):
            Score([])


if __name__ == '__main__':

    unittest.main()
