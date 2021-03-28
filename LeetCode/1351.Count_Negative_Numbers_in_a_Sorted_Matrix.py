from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            i = len(row) - 1
            while i >= 0 and row[i] < 0:
                i -= 1
            count += len(row) - i - 1
        return count


class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        i, j = 0, n - 1
        count = 0

        while i < m and j >= -1:
            if j >= 0 and grid[i][j] < 0:
                j -= 1
            else:
                count += n - j - 1
                i += 1
        return count
