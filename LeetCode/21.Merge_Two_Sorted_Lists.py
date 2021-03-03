# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        pointer1 = l1
        pointer2 = l2

        # determine which list to start with
        if l1.val < l2.val:
            head = l1
            last = l1
            pointer1 = l1.next
        else:
            head = l2
            last = l2
            pointer2 = l2.next

        while not (pointer1 is None or pointer2 is None):
            if pointer1.val < pointer2.val:
                last, pointer1 = self.link(last, pointer1)
            else:
                last, pointer2 = self.link(last, pointer2)

        if pointer1 is None:
            last.next = pointer2

        if pointer2 is None:
            last.next = pointer1

        return head

    @staticmethod
    def link(last, pointer):
        if last.next != pointer:
            last.next = pointer

        last = pointer
        pointer = pointer.next
        return last, pointer


class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
