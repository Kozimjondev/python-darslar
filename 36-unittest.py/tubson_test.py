import unittest 
from tubson import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))

    def test_false(self):
        self.assertFalse(tubSonmi(12))

unittest.main()



