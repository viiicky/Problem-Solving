from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        response = []
        for candy in candies:
            response.append(candy + extraCandies >= max_candies)
        return response
