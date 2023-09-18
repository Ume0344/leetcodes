import unittest
import linked_list


class TestStringManipulation(unittest.TestCase):
    def test_insert_at_start(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)

        assert head.data == 6

    def test_insert_at_end(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)

        linked_list.insert_at_end(7, head)
        
        while head.next_node is not None:
            head = head.next_node

        assert head.data == 7

    def test_insert_after_specific_node(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)
        head = linked_list.insert_at_start(78, head)

        linked_list.insert_after_specific_node(54, head, 6)
        
        while head.data != 54:
            head = head.next_node

        assert head.data == 54

    def test_reverse_linked_list(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)
        head = linked_list.insert_at_start(78, head)
        head = linked_list.insert_at_start(54, head)

        linked_list.print_list(head)
        head_rev = linked_list.reverse_linked_list(head)
        linked_list.print_list(head_rev)


        assert head_rev.data == 5


if __name__ == '__main__':
    unittest.main()
