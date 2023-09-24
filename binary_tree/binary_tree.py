from typing import List
class Node:
    def __init__(self, data) -> None:
        self.data: Any = data
        self.right : Node = None
        self.left: Node = None

def create_binary_node() -> Node:
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f 

    """
             a
           /   \
          b     c
        /   \    \
       d     e    f

    """

    return a

def print_tree(root: Node) -> None:
    print(root.data)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)

def depth_first_value(root: Node, values_array: List) -> List:
    """
    Traverse through binary tree depthwise. Can be done by using recursion and stack.
    Prefer to do with recursion

    param root: Root of the tree
    param values_array: Array to store values of tree nodes.
    return list of values of binary tree nodes.
    """
    if root == None:
        return values_array
    values_array.append(root.data)
    if root.left:
        depth_first_value(root.left, values_array)
    if root.right:
        depth_first_value(root.right, values_array)
    
    return values_array

