from typing import List
from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for n1 in nums1:
            pos = nums2.index(n1)
            for n2 in nums2[pos+1:]:
                if n2 > n1:
                    output.append(n2)
                    break
            else:
                output.append(-1)

        return output


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_numbers = {}
        numbers_to_process = deque()

        for num in nums2:
            while len(numbers_to_process) > 0 and numbers_to_process[-1] < num:
                greater_numbers[numbers_to_process.pop()] = num
            numbers_to_process.append(num)

        output = []
        for num in nums1:
            output.append(greater_numbers.get(num, -1))
        return output
