from collections import defaultdict
from typing import List
import heapq


def heappush(heap, item):
    return heapq.heappush(heap, -item)


def heappushpop(heap, item):
    return heapq.heappushpop(heap, -item)


def heappop(heap):
    return -heapq.heappop(heap)


def heapmax(heap):
    return -heap[0]


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
            if value < heapmax(heap):
                heappushpop(heap, value)

        return [(heappop(heap)).pos for _ in range(k)][::-1]


class Solution2:
    # Time complexity: O(m logn + m logm)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i in range(k):
            row = Row(count_ones(mat[i]), i)
            heappush(heap, row)

        for row_pos, row_value in enumerate(mat[k:], start=k):
            value = Row(count_ones(row_value), row_pos)
            if value < heapmax(heap):
                heappushpop(heap, value)

        return [(heappop(heap)).pos for _ in range(k)][::-1]


class Solution3:
    # Time complexity: O(mn + m logm) amortised
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = defaultdict(list)
        for pos, row in enumerate(mat):
            count = sum(row)
            counts[count].append(pos)

        output = []
        for key in sorted(counts):
            values = counts[key]
            for value in values:
                output.append(value)
                if len(output) == k:
                    return output


class Solution4:
    # Time complexity: O(m logn + m logm) amortised
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = defaultdict(list)
        for pos, row in enumerate(mat):
            count = count_ones(row)
            counts[count].append(pos)

        output = []
        for key in sorted(counts):
            values = counts[key]
            for value in values:
                output.append(value)
                if len(output) == k:
                    return output


def count_ones(items):
    start = real_start = 0
    end = real_end = len(items) - 1

    while True:
        mid = (start + end) // 2
        if (items[mid] == 1 and mid == real_end) or (items[mid] == 1 and items[mid + 1] == 0):
            return mid + 1
        elif items[mid] == 1:
            start = mid + 1
        elif items[mid] == 0 and mid == real_start:
            return mid
        elif items[mid] == 0:
            end = mid - 1
