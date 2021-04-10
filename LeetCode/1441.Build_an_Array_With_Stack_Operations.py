from collections import deque
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        next_number = 1
        stack = deque()
        operations = []

        for _ in range(target[0] - 1):
            stack.append(next_number)
            next_number += 1
            operations.append('Push')
            operations.append('Pop')

        target_iter = iter(target)
        t = next(target_iter)

        try:
            while True:
                if len(stack) == 0 or t - 1 == stack[-1]:
                    stack.append(next_number)
                    next_number += 1
                    operations.append('Push')
                    t = next(target_iter)
                else:
                    stack.append(next_number)
                    next_number += 1
                    operations.append('Push')
                    operations.append('Pop')
        except StopIteration:
            return operations
