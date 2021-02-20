from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # traverse the array
        # for each item, count how many other items it is bigger from
        # put in the result array
        # return the result array

        frequencies = []
        for current in nums:
            count = 0
            for other in nums:
                if current > other:
                    count += 1
            frequencies.append(count)
        return frequencies


class Solution2:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # store the sorted version of nums somewhere
        sorted_nums = sorted(nums)

        # iterate this sorted array and create num frequencies
        frequencies = {}
        for position, num in enumerate(sorted_nums):
            if num not in frequencies:
                frequencies[num] = position

        # iterate the original array and prepare result
        result = []
        for num in nums:
            result.append(frequencies[num])

        return result


class Solution3:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # prepare frequency array
        frequencies = [0] * 101
        for num in nums:
            frequencies[num] += 1

        # traverse the frequency array and prepare result map
        result_map = {}
        total = 0
        for number, count in enumerate(frequencies):
            result_map[number] = total
            total = total + count

        # traverse the nums array and prepare the result
        result = []
        for num in nums:
            result.append(result_map[num])

        return result
