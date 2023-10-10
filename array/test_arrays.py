import unittest
from arrays import Array

class TestArray(unittest.TestCase):
    def test_group_anagrams(self):
        a = Array()
        word_list = ["eat","tea","tan","ate","nat","bat"]
        grouped_list = a.groupAnagrams(word_list)

        assert grouped_list == [["eat","tea","ate"],["tan","nat"],["bat"]]

if __name__ == '__main__':
    unittest.main()