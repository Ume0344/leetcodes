import unittest
import binary_tree


class TestBinaryTree(unittest.TestCase):
    def test_depth_first_value_recursion(self):
        root = binary_tree.create_binary_node()
        values = []
        values = binary_tree.depth_first_value_recursion(root, values)

        assert values == [1, 2, 4, 8, 12, 5, 9, 3, 6, 10, 7, 11]
    
    def test_depth_first_value_stack(self):
        root = binary_tree.create_binary_node()
        values = binary_tree.depth_first_value_stack(root)

        assert values == [1, 2, 4, 8, 12, 5, 9, 3, 6, 10, 7, 11]

    def test_breadth_first_value(self):
        root = binary_tree.create_binary_node()
        values = binary_tree.breadth_first_value(root)

        assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    
if __name__ == '__main__':
    unittest.main()
