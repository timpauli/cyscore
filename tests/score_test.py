import tempfile as tf
import unittest

from cyscore import Score

from .cyscore_test import CyscoreTest


class ScoreTest(CyscoreTest):

    def test_repr(self):
        result = str(self.score_dummy)
        self.assertEqual(result, self.score_correct)

    def test_init_len(self):
        with self.assertRaises(AssertionError):
            Score([])

    def test_to_file(self):
        name = tf.gettempdir() + '/test.sco'
        self.score_dummy.to_file(name)
        with open(name) as f:
            result = f.read()
            self.assertEqual(result, self.score_correct)

    def test_render(self):
        name = tf.gettempdir() + '/test.'
        sconame = name + 'sco'
        orcname = name + 'orc'
        outname = name + 'wav'
        self.score_dummy.render(orcname, sconame, outname)
        # no real checking..


if __name__ == '__main__':

    unittest.main()
