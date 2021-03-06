# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()

        current_a = headA
        while current_a is not None:
            nodes.add(current_a)
            current_a = current_a.next

        current_b = headB
        while current_b is not None:
            if current_b in nodes:
                return current_b
            current_b = current_b.next

        return None


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # find the length of list A
        len_a = self.length(headA)

        # find the length of list B
        len_b = self.length(headB)

        # figure out where to start from in each of the list
        offset = abs(len_a - len_b)
        if len_a > len_b:
            pointer_b = headB
            pointer_a = self.offset(headA, offset)
        else:
            pointer_a = headA
            pointer_b = self.offset(headB, offset)

        # traverse the two list together and find the intersection
        while pointer_a is not None and pointer_b is not None:
            if pointer_a == pointer_b:
                return pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        return None

    @staticmethod
    def length(node):
        length = 0

        current = node
        while current is not None:
            length += 1
            current = current.next

        return length

    @staticmethod
    def offset(node, offset):
        while offset > 0:
            node = node.next
            offset -= 1
        return node
