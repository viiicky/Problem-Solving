# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, total=0):
        self.total = total

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0

        if low <= root.val <= high:
            self.total += root.val

        if root.val > low:
            self.rangeSumBST(root.left, low, high)  # go to left

        if root.val < high:
            self.rangeSumBST(root.right, low, high)  # go to right

        return self.total
