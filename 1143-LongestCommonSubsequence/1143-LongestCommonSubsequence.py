# Last updated: 8/21/2026, 2:45:35 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4        dp = [[0] * (n + 1) for _ in range(m + 1)]
5
6        for i in range(m - 1, -1, -1):
7            for j in range(n - 1, -1, -1):
8                if text1[i] == text2[j]:
9                    dp[i][j] = 1 + dp[i + 1][j + 1]
10                else:
11                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
12
13        return dp[0][0]