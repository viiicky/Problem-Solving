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


class Solution2:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                total += node.val

            if node.val > low and node.left:
                stack.append(node.left)

            if node.val < high and node.right:
                stack.append(node.right)

        return total
