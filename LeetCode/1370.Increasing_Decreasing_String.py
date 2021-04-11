from collections import defaultdict


class Solution:
    def sortString(self, s: str) -> str:
        counts = defaultdict(lambda: 0)
        for char in s:
            counts[char] += 1

        letters = 'abcdefghijklmnopqrstuvwxyz'
        result = []
        while len(result) != len(s):
            for letter in letters:
                if counts[letter] > 0:
                    result.append(letter)
                    counts[letter] -= 1

            for letter in letters[::-1]:
                if counts[letter] > 0:
                    result.append(letter)
                    counts[letter] -= 1

        return ''.join(result)
