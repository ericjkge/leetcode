# Last updated: 6/28/2025, 3:02:18 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(i, j):
            if i == 0 or j == 0:
                return 1
            return dp(i - 1, j) + dp(i, j - 1)

        return dp(m - 1, n - 1)