# Last updated: 6/28/2025, 3:06:29 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == 0 or j == 0:
                return 1
            memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
            return memo[(i, j)]

        return dp(m - 1, n - 1)