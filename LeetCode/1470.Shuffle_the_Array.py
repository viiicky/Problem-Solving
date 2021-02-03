from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        response = []
        for i in range(n):
            response.append(nums[i])
            response.append(nums[i+n])
        return response
