# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Time complexity: O(n)
        Space complexity: O(1)
        where n = number of nodes in the list
        """

        temp = prev = node
        while temp.next:
            temp.val = temp.next.val
            prev = temp
            temp = temp.next

        prev.next = None


class Solution2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        Time complexity: O(1)
        Space complexity: O(1)
        """

        node.val = node.next.val
        node.next = node.next.next
