# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous_guy = None
        current_guy = head

        while current_guy:
            next_guy = current_guy.next  # first, safe-guard the next item
            current_guy.next = previous_guy  # then, do the action, i.e. reverse the link
            previous_guy = current_guy  # catch-up: bring previous guy one step ahead
            current_guy = next_guy  # catch-up: bring current guy one step ahead

        return previous_guy


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        reversed_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversed_list
