class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_set = set(jewels)
        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count
