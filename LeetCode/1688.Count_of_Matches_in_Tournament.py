import unittest


class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches_played = 0
        teams_advanced = n

        while teams_advanced > 1:
            matches_played = teams_advanced // 2
            total_matches_played += matches_played
            teams_advanced = matches_played + (teams_advanced % 2)

        return total_matches_played


class SolutionTest(unittest.TestCase):
    def test_number_of_matches(self):
        sol = Solution()
        self.assertEqual(sol.numberOfMatches(7), 6)


if __name__ == '__main__':
    unittest.main()
