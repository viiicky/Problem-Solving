from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, queue, level):
            queue.append(node)

            while len(queue) > 0:
                current = queue.popleft()
                for child in current.children:
                    dfs(child, queue, level + 1)

                levels.append(level)

        if root is None:
            return 0
        levels = []
        dfs(root, deque(), 1)

        return max(levels)
