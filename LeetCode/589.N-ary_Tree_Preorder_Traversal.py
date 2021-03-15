from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self._preorder(root, [])

    def _preorder(self, current_node, all_nodes):
        if current_node is None:
            return

        all_nodes.append(current_node.val)

        for child in current_node.children:
            self._preorder(child, all_nodes)

        return all_nodes


class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        nodes_stack = [root]
        all_nodes = []

        while len(nodes_stack) > 0:
            current_node = nodes_stack.pop()

            if current_node is not None:
                all_nodes.append(current_node.val)
                nodes_stack.extend(current_node.children[::-1])

        return all_nodes
