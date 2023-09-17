class Node:
    def __init__(self) -> None:
        self.data = None
        self.next_node = None


def insert_at_start(data, head_ref) -> Node:
    """
    Insert node at start of linked list.

    param data: Data to be stored at start of linked list
    param head_ref: Head reference of linked list

    return head_ref: Updated head reference
    """
    node = Node()
    node.data = data
    node.next_node = head_ref
    head_ref = node

    return head_ref


def insert_at_end(data, node: Node) -> None:
    """
    Insert node at end of linked list.

    param data: Data to be stored at start of linked list
    param node: Head referenced node of linked list
    """
    new_node = Node()

    new_node.data = data
    new_node.next_node = None
   
    while node.next_node is not None:
        node = node.next_node
    
    node.next_node = new_node
    

def insert_after_specific_node(data, node, specific_position) -> None:
    """
    Insert node after specific node in linked list.

    param data: Data to be stored.
    param node: Head referenced node of linked list
    """
    new_node = Node()

    while node.data is not specific_position:
        node = node.next_node

    new_node.data = data
    new_node.next_node = node.next_node
    node.next_node = new_node


def print_list(node: Node):
    """
    Print linked list.
    
    param node: Head referenced node.
    """
    while node is not None:
        print(node.data)
        node = node.next_node
