# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    where n = size of linked list
    """
    def getDecimalValue(self, head: ListNode) -> int:
        digits = []
        temp = head
        while temp is not None:
            digits.append(temp.val)
            temp = temp.next

        total = 0
        for i, val in enumerate(digits[::-1]):
            total += val * (2 ** i)

        return total


class Solution2:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    where n = size of linked list
    """
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0

        temp = head
        while temp is not None:
            number = (number * 2) + temp.val
            temp = temp.next

        return number


class Solution3:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    where n = size of linked list

    Same as above; just some fancy bit magic happening
    """
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0

        temp = head
        while temp is not None:
            number = (number << 1) | temp.val
            temp = temp.next

        return number
