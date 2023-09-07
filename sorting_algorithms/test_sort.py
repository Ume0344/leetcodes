import unittest
from sort import Sort


class TestSum(unittest.TestCase):
    def test_bubble_sort(self):
        # Run this command to run test `python3 -m unittest test_hash_map.py`
        s = Sort()
        arr = [3,2,1,6,4,5]
        arr1 = [66,43,27,56,222,102]

        arr_sort = s.bubble_sort(arr)
        arr1_sort = s.bubble_sort(arr1)

        assert arr_sort == [1, 2, 3, 4, 5, 6]
        assert arr1_sort == [27, 43, 56, 66, 102, 222]

if __name__ == '__main__':
    unittest.main()
