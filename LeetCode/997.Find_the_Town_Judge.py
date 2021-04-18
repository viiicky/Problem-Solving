from typing import List
from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        trust_count = defaultdict(lambda: 0)
        trusters = set()

        for truster, trustee in trust:
            trust_count[trustee] += 1
            trusters.add(truster)

        for trustee, count in trust_count.items():
            if count == N - 1 and trustee not in trusters:
                return trustee
        else:
            return -1
