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

root = create_binary_node()
print_tree(root)
