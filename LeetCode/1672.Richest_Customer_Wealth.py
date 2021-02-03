from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for banks in accounts:
            wealth = sum(banks)
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth
