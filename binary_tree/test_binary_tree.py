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

    def test_tree_includes_stack(self):
        root = binary_tree.create_binary_node()
        value = 12

        flag = binary_tree.tree_includes_stack(root, value)
        assert flag == True
    
    def test_tree_doesnot_include_stack(self):
        root = binary_tree.create_binary_node()
        value = 120

        flag = binary_tree.tree_includes_stack(root, value)
        assert flag == False
    
    def test_tree_includes_recursive(self):
        root = binary_tree.create_binary_node()
        value = 6

        flag = binary_tree.tree_includes_recursive(root, value)
        assert flag == True
    
    def test_tree_doesnot_include_recursive(self):
        root = binary_tree.create_binary_node()
        value = 61

        flag = binary_tree.tree_includes_recursive(root, value)
        assert flag == False

    def test_tree_sum_recursion(self):
        root = binary_tree.create_binary_node()

        sum = binary_tree.tree_sum_recursion(root)
        assert sum == 78

    def test_tree_sum_stack(self):
        root = binary_tree.create_binary_node()

        sum = binary_tree.tree_sum_stack(root)
        assert sum == 78

    def test_tree_min_value(self):
        root = binary_tree.create_binary_node()

        min = binary_tree.tree_min_value(root)
        assert min == 1
    
    def test_tree_min_value_root_null(self):
        root = None

        min = binary_tree.tree_min_value(root)
        assert min == float('inf')
    
    def test_tree_max_path_value(self):
        root = binary_tree.create_binary_node()

        sum = binary_tree.tree_max_path_value(root)
        assert sum == 27
    

    def test_tree_max_depth(self):
        root = binary_tree.create_binary_node()

        depth = binary_tree.tree_max_depth(root)
        assert depth == 5

    
    def test_invert_tree(self):
        root = binary_tree.create_binary_node()

        root = binary_tree.invert_tree(root)
        values = binary_tree.breadth_first_value(root)

        assert values == [1, 3, 2, 7, 6, 5, 4, 11, 10, 9, 8, 12]

    def test_trees_are_identical(self):
        root1 = binary_tree.create_binary_node()
        root2 = binary_tree.create_binary_node()

        flag = binary_tree.trees_are_identical(root1, root2)
        assert flag == True

    def test_trees_are_not_identical(self):
        root1 = binary_tree.create_binary_node()
        root2 = None

        flag = binary_tree.trees_are_identical(root1, root2)
        assert flag == False
    
    def test_trees_are_identical_recursion(self):
        root1 = binary_tree.create_binary_node()
        root2 = binary_tree.create_binary_node()

        flag = binary_tree.trees_are_identical_recursion(root1, root2)
        assert flag == True
    
    def test_trees_are_identical_recursion(self):
        root1 = binary_tree.create_binary_node()
        subRoot = binary_tree.create_sub_binary_node()

        flag = binary_tree.isSubTree(root1, subRoot)
        assert flag == False
    
    
if __name__ == '__main__':
    unittest.main()
