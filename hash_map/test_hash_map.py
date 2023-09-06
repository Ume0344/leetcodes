import unittest
from hash_map import HashMap


class TestSum(unittest.TestCase):
    def test_hash_map(self):
        # Run this command to run test `python3 -m unittest test_hash_map.py`
        h = HashMap(10)
        h.put("apple", 10)
        h.put("banana", 15)
        h.put("paple", 20)
        h.put("alppe", 40)

        value = h.get("apple")
        value1 = h.get("banana")
        value2 = h.get("paple")
        value3 = h.get("alppe")

        assert value == 10
        assert value1 == 15
        assert value2 == 20
        assert value3 == 40


if __name__ == '__main__':
    unittest.main()
