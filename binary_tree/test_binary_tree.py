import unittest
import binary_tree

class TestBinaryTree(unittest.TestCase):
    def test_depth_first_value(self):
        root = binary_tree.create_binary_node()
        values = []
        values = binary_tree.depth_first_value(root, values)

        assert values == [1, 2, 4, 5, 3, 6]
    
if __name__ == '__main__':
    unittest.main()
