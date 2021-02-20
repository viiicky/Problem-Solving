from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique_map = {}
        for num in nums:
            if num not in unique_map:
                unique_map[num] = True
            elif unique_map[num] is True:
                unique_map[num] = False

        total = 0
        for key, value in unique_map.items():
            if value:
                total += key

        return total


class Solution2:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniques = set()
        duplicates = set()

        for num in nums:
            if num not in duplicates:
                if num in uniques:
                    uniques.remove(num)
                    duplicates.add(num)
                else:
                    uniques.add(num)

        return sum(uniques)
