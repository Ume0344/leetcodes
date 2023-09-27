from typing import List, Any


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
    g = Node(7)
    h = Node(8)
    i = Node(9)
    j = Node(10)
    k = Node(11)
    l = Node(12)


    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h
    h.left = l
    e.right = i
    f.left = j
    g.right = k


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


def depth_first_value_recursion(root: Node, values_array: List) -> List:
    """
    Traverse through binary tree depthwise. It can be done by using recursion and stack.
    We prefer to do with recursion. Under the hood of recursion, we are anyways using stack
    so same answers are expected.

    param root: Root of the tree
    param values_array: Array to store values of tree nodes.
    return list of values of binary tree nodes.
    """
    if root == None:
        return values_array
    values_array.append(root.data)
    if root.left:
        depth_first_value_recursion(root.left, values_array)
    if root.right:
        depth_first_value_recursion(root.right, values_array)
    
    return values_array


def depth_first_value_stack(root: Node) -> List:
    """
    Traverse through binary tree depthwise with stacks..

    param root: Root of the tree
    param values_array: Array to store values of tree nodes.
    return list of values of binary tree nodes.
    """
    values_array: List = []
    if root == None:
        return values_array
    
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        values_array.append(current.data)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return values_array


def breadth_first_value(root: Node) -> List:
    """
    Traverse through binary tree breadth wise. Can be done by using recursion and queue.
    Prefer to do with queue. There is no straight forward solution with recursion as resursion uses
    stack under the hood and we need queue to solve it.

    param root: Root of the tree
    param values_array: Array to store values of tree nodes.
    return list of values of binary tree nodes.
    """
    # go to root, put data into value
    # go to root.left, put data
    # go to root.right, put data
    # again go to left, make it a new root and repeat the process.
    # go to right, make it new root and repeat the process.
    '''
    This solution can work if tree depth is 2, after words it wont work. Need 
    alot of checks to make it work.
    if root == None:
        return values_array
    
    if root and i == 0:
        values_array.append(root.data)

    if root.left:
        values_array.append(root.left.data)

    if root.right:
        values_array.append(root.right.data)
    i +=1
    breadth_first_value(root.left, values_array, i)
    breadth_first_value(root.right, values_array, i)
    '''
    values_array: List = []

    if root is None:
        return values_array

    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        values_array.append(current.data)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return values_array


def tree_includes_stack(root: Node, value: Any) -> bool:
    """
    Finds if tree has a particular value/data (through stack and DFS).

    param root: Root of the binary tree.
    param value: Value to be found 

    return bool
    """
    flag = False 
    if root is None:
        return flag
    
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.data == value:
            flag = True 
            break
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return flag


def tree_includes_recursive(root: Node, value: Any) -> bool:
    """
    Finds if tree has a particular value/data (recursively).

    param root: Root of the binary tree.
    param value: Value to be found 

    return bool
    """
    flag = False 
    if root is None:
        return flag

    if root.data == value:
        flag = True
        return flag
    return tree_includes_recursive(root.left, value) or tree_includes_recursive(root.right, value)


def tree_sum_recursion(root: Node) -> int:
    if root is None:
        return 0
    return root.data + tree_sum_recursion(root.left) + tree_sum_recursion(root.right)

    
def tree_sum_stack(root: Node) -> int:
    sum = 0
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        sum += current.data
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return sum
