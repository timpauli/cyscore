from cyscore_test import CyscoreTest


class VoiceTest(CyscoreTest):

    def test_repr(self):
        result = str(self.voice_dummy)
        self.assertEqual(result, self.voice_correct)


if __name__ == '__main__':

    unittest.main()
