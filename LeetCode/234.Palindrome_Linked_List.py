import unittest
from math import ceil


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Space: O(n)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        array = []
        current = head

        while current is not None:
            array.append(current.val)
            current = current.next

        i, j = 0, len(array) - 1
        while True:
            if j < i:
                return True

            if array[i] != array[j]:
                return False

            i, j = i + 1, j - 1


# Time: O(n)
# Space: O(1)
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        # find the length of the list
        current = head
        size = 0
        while current is not None:
            size += 1
            current = current.next

        # set up a marker in the middle of the list
        mid = ceil(size / 2)
        mid_node = head
        for _ in range(mid):
            mid_node = mid_node.next

        # reverse the second half of the list
        tail = self.reverse_list(mid_node)

        # start comparing items from the start of the list and the tail of the actual list, one by one
        start_node = head
        end_node = tail

        palindrome = True
        while end_node is not None:
            if start_node.val != end_node.val:
                palindrome = False
                break
            start_node = start_node.next
            end_node = end_node.next

        # optional: bring the list back in original form
        # self.reverse_list(tail)

        return palindrome

    @staticmethod
    def reverse_list(node):
        current = node
        prev = None

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev

    @staticmethod
    def print_list(node):
        output = ''
        temp = node
        while temp is not None:
            output += str(temp.val) + ' -> '
            temp = temp.next
        print(output)


class PalindromeLinkedListTest(unittest.TestCase):
    def setUp(self):
        # self.solution = Solution()
        self.solution = Solution2()

    def test_palindrome_even(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)

        self.assertEqual(True, self.solution.isPalindrome(head))

    def test_palindrome_odd(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(1)

        self.assertEqual(True, self.solution.isPalindrome(head))

    def test_not_palindrome_even(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(1)
        head.next.next.next = ListNode(1)
        self.assertEqual(False, self.solution.isPalindrome(head))

    def test_not_palindrome_odd(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)

        self.assertEqual(False, self.solution.isPalindrome(head))

    def test_palindrome_size_two(self):
        head = ListNode(1)
        head.next = ListNode(1)

        self.assertEqual(True, self.solution.isPalindrome(head))

    def test_not_palindrome_size_two(self):
        head = ListNode(1)
        head.next = ListNode(2)

        self.assertEqual(False, self.solution.isPalindrome(head))

    def test_palindrome_size_one(self):
        head = ListNode(1)

        self.assertEqual(True, self.solution.isPalindrome(head))

    def test_palindrome(self):
        head = ListNode('a')
        head.next = ListNode('b')
        head.next.next = ListNode('c')
        head.next.next.next = ListNode('d')
        head.next.next.next.next = ListNode('d')
        head.next.next.next.next.next = ListNode('c')
        head.next.next.next.next.next.next = ListNode('b')
        head.next.next.next.next.next.next.next = ListNode('a')

        self.assertEqual(True, self.solution.isPalindrome(head))


if __name__ == '__main__':
    unittest.main()
