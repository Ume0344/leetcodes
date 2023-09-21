from typing import List


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


def reverse_linked_list(head_ref: Node) -> Node:
    """
    Reverse the linked list

    param linked_list: linked list to be reversed
    return : Reversed linked list.
    """
    previous = None
    current = head_ref

    while current is not None:
        next = current.next_node
        current.next_node = previous
        previous = current
        current = next

    head_ref = previous

    return head_ref


def delete_node(node: Node, data) -> Node:
    """
    Delete a node from linked list.

    param node: Head referenced node.
    param data: Data containing node to be delete
    return head_ref: Head reference of Linked list
    """
    head_ref = node

    if data == head_ref.data:
        head_ref = head_ref.next_node
    else:
        while node.data is not data:
            prev = node
            node = node.next_node
        prev.next_node = node.next_node

    return head_ref


def merge_two_linked_list(linkedlist1: Node, linkedlist2: Node) -> Node:
    """
    Merges two sorted linkedlists
    Idea is to create a temp node and append it with nodes from linkedlist1 and linkedlist2.
    if linkedlist1.data is smaller, temp.next_node = linkedlist1, otherwise temp.next_node = linkedlist2.

    param linkedlist1: First sorted linkedlist to be merged.
    param linkedlist2: Second sorted linkedlist to be merged.
    returns dummy.next_node: Merged linkedlist
    """
    temp = Node()
    dummy = temp

    while linkedlist1 and linkedlist2:
        if linkedlist1.data <= linkedlist2.data:
            temp.next_node = linkedlist1
            temp = temp.next_node
            linkedlist1 = linkedlist1.next_node
        else:
            temp.next_node = linkedlist2
            temp = temp.next_node
            linkedlist2 = linkedlist2.next_node

        if linkedlist1 is not None:
            temp.next_node = linkedlist1
        if linkedlist2 is not None:
            temp.next_node = linkedlist2

    return dummy.next_node


def print_list(node: Node):
    """
    Print linked list.
    
    param node: Head referenced node.
    """
    while node is not None:
        print(node.data)
        node = node.next_node
    print("****")
