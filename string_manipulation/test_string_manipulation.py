import unittest
from string_manipulation import StringManipulation


class TestStringManipulation(unittest.TestCase):
    def test_reverse_string(self):

        s = StringManipulation()
        string = s.reverse_string("hello")

        assert string == "olleh"

if __name__ == '__main__':
    unittest.main()
