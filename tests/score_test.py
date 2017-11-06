from cyscore_test import CyscoreTest


class ScoreTest(CyscoreTest):

    def test_repr(self):
        result = str(self.score_dummy)
        self.assertEqual(result, self.score_correct)


if __name__ == '__main__':

    unittest.main()
