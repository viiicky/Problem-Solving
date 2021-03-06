# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = set()

        current = head
        while current is not None:
            if current in nodes:
                return True
            nodes.add(current)
            current = current.next

        return False


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        slow_pointer = fast_pointer = head
        while slow_pointer is not None and fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if slow_pointer == fast_pointer:
                return True

        return False
