class Node:
    def __init__(self) -> None:
        self.data = None
        self.next_node = None

def insert_at_start(data, head_ref):
    node = Node()
    node.data = data
    node.next_node = head_ref
    head_ref = node

    return head_ref

def print_list(node: Node):
    while node is not None:
        print(node.data)
        node = node.next_node

head = None

head = insert_at_start(5, head)
head = insert_at_start(6, head)
head = insert_at_start(7, head)

print_list(head)
