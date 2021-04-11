from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled_string_chars = [None] * len(indices)

        for index, char in zip(indices, s):
            shuffled_string_chars[index] = char

        return ''.join(shuffled_string_chars)
