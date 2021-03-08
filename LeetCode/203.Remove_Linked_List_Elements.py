import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next

        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def _validate_list(self, node, key, expected_size):
        actual_size = 0
        while node:
            actual_size += 1
            if node.val == key:
                self.assertTrue(False)
            node = node.next
        self.assertEqual(expected_size, actual_size)

    def test_remove_last_element(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)

        new_head = self.solution.removeElements(head, 6)
        self._validate_list(new_head, 6, 2)

    def test_remove_first_element(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)

        new_head = self.solution.removeElements(head, 1)
        self._validate_list(new_head, 1, 2)

    def test_remove_multiple_values(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(6)
        head.next.next.next.next.next = ListNode(5)

        new_head = self.solution.removeElements(head, 6)
        self._validate_list(new_head, 6, 4)

    def test_remove_two_continuous_values(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(6)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(4)

        new_head = self.solution.removeElements(head, 6)
        self._validate_list(new_head, 6, 4)

    def test_remove_three_continuous_values(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(6)
        head.next.next.next.next = ListNode(6)
        head.next.next.next.next.next = ListNode(5)

        new_head = self.solution.removeElements(head, 6)
        self._validate_list(new_head, 6, 3)

    def test_remove_continuous_values_at_end(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(6)
        head.next.next.next = ListNode(6)

        new_head = self.solution.removeElements(head, 6)
        self._validate_list(new_head, 6, 2)

    def test_remove_continuous_values_in_beginning(self):
        head = ListNode(1)
        head.next = ListNode(1)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(2)

        new_head = self.solution.removeElements(head, 1)
        self._validate_list(new_head, 1, 2)

    def test_remove_zero_values(self):
        head = ListNode(1)
        head.next = ListNode(2)

        new_head = self.solution.removeElements(head, 10)
        self._validate_list(new_head, 10, 2)

    def test_remove_from_empty_list(self):
        head = None

        new_head = self.solution.removeElements(head, 1)
        self._validate_list(new_head, 1, 0)

    def test_remove_all_values(self):
        head = ListNode(7)
        head.next = ListNode(7)
        head.next.next = ListNode(7)
        head.next.next.next = ListNode(7)

        new_head = self.solution.removeElements(head, 7)
        self._validate_list(new_head, 7, 0)


if __name__ == '__main__':
    unittest.main()
