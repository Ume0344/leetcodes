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

        head_rev = linked_list.reverse_linked_list(head)

        assert head_rev.data == 5
        
    def test_delete_starting_node(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)
        head = linked_list.insert_at_start(78, head)
        head = linked_list.insert_at_start(54, head)

        head = linked_list.delete_node(head, 54)

        assert head.data == 78

    def test_delete_middle_node(self):
        head = None
        head = linked_list.insert_at_start(5, head)
        head = linked_list.insert_at_start(6, head)
        head = linked_list.insert_at_start(78, head)
        head = linked_list.insert_at_start(54, head)

        head = linked_list.delete_node(head, 6)

    def test_merge_two_linked_list(self):
        head = None
        head1 = None

        head = linked_list.insert_at_start(45, head)
        head = linked_list.insert_at_start(34, head)
        head = linked_list.insert_at_start(23, head)
        head = linked_list.insert_at_start(10, head)

        head1 = linked_list.insert_at_start(35, head1)
        head1 = linked_list.insert_at_start(27, head1)
        head1 = linked_list.insert_at_start(25, head1)
        head1 = linked_list.insert_at_start(12, head1)

        linked_list.print_list(head)
        linked_list.print_list(head1)

        head_merged = linked_list.merge_two_linked_list(head, head1)
        print("Merged list is")
        linked_list.print_list(head_merged)
        head_merged_next = head_merged.next_node

        assert head_merged.data == 10
        assert head_merged_next.data == 12

if __name__ == '__main__':
    unittest.main()
