import unittest
from arrays import Array

class TestArray(unittest.TestCase):
    def test_group_anagrams(self):
        a = Array()
        word_list = ["eat","tea","tan","ate","nat","bat"]
        grouped_list = a.groupAnagrams(word_list)

        assert grouped_list == [["eat","tea","ate"],["tan","nat"],["bat"]]

    def test_topKFrequent(self):
        a = Array()
        nums = [1,1,1,2,2,3]
        k = 2
        top_k = a.topKFrequent(nums, k)

        assert top_k == [1,2]

if __name__ == '__main__':
    unittest.main()
