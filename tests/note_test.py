from cyscore_test import CyscoreTest


class NoteTest(CyscoreTest):

    def test_repr(self):
        result = str(self.note_dummy)
        self.assertEqual(result, self.note_correct)


if __name__ == '__main__':

    unittest.main()
