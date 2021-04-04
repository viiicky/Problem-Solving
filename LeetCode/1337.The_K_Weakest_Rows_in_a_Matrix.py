from typing import List
import heapq


def heappush(heap, item):
    return heapq.heappush(heap, -item)


def heappushpop(heap, item):
    return heapq.heappushpop(heap, -item)


def heappop(heap):
    return heapq.heappop(heap)


class Row:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos

    def __lt__(self, other):
        return self.pos < other.pos if self.value == other.value else self.value < other.value

    def __neg__(self):
        return Row(-self.value, -self.pos)

    def __repr__(self):
        return f'value: {self.value}, pos: {self.pos}'


class Solution:
    # Time complexity: O(mn + m logm)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(k):
            row = Row(sum(mat[i]), i)
            heappush(heap, row)

        for row_pos, row_value in enumerate(mat[k:], start=k):
            value = Row(sum(row_value), row_pos)
            if value < -heap[0]:
                heappushpop(heap, value)

        return [(-heappop(heap)).pos for _ in range(k)][::-1]
