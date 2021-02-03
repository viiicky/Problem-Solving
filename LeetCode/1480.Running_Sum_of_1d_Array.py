from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = [nums[0]]
        for i in range(1, len(nums)):
            running_sums.append(nums[i] + running_sums[i-1])
        return running_sums
