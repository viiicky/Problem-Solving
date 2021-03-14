# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


class Solution2:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        stack = []
        if root1 is not None and root2 is not None:
            stack.append((root1, root2))
        elif root1 is None:
            root1 = root2

        while len(stack) > 0:
            tree1_node, tree2_node = stack.pop()
            tree1_node.val += tree2_node.val

            # left case
            if tree1_node.left is not None and tree2_node.left is not None:
                stack.append((tree1_node.left, tree2_node.left))
            elif tree1_node.left is None:
                tree1_node.left = tree2_node.left

            # right case
            if tree1_node.right is not None and tree2_node.right is not None:
                stack.append((tree1_node.right, tree2_node.right))
            elif tree1_node.right is None:
                tree1_node.right = tree2_node.right

        return root1
