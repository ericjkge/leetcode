# Last updated: 8/21/2026, 2:30:44 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [[1] * n for _ in range(m)]
4
5        for i in range(m - 2, -1, -1):
6            for j in range(n - 2, -1, -1):
7                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
8
9        return dp[0][0]