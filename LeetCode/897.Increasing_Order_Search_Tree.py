from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inorder(node: TreeNode, result_nodes: List[TreeNode]):
            if not node:
                return

            inorder(node.left, result_nodes)
            result_nodes.append(TreeNode(node.val))
            inorder(node.right, result_nodes)

            return result_nodes

        # traverse the tree in inorder and create a tree out of it
        nodes = []
        nodes = inorder(root, nodes)

        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]

        return nodes[0]


class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: TreeNode):
            if not node:
                return

            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        # traverse the tree in inorder and create a tree out of it
        start = current = TreeNode()
        for val in inorder(root):
            current.right = TreeNode(val)
            current = current.right

        return start.right


class Solution3:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node: TreeNode):
            if not node:
                return

            yield from inorder(node.left)
            yield node
            yield from inorder(node.right)

        start = prev = None
        for position, item in enumerate(inorder(root)):
            if position == 0:
                start = prev = item
            else:
                prev.right = item
                item.left = None
                prev = item

        return start
