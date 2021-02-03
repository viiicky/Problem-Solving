from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        sums = {}
        for num in nums:
            sums[num] = sums.get(num, 0) + 1
        for count in sums.values():
            total += ((count - 1) * count) // 2
        return total


class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        total = 0
        sums = [0] * 100
        for num in nums:
            sums[num - 1] = sums[num - 1] + 1
        for count in sums:
            total += ((count - 1) * count) // 2
        return total
