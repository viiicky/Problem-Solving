# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # start from the root
        # find the max of height of both of the subtrees
        # and at 1 to that

        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
