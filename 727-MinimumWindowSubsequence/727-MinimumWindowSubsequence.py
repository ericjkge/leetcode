# Last updated: 1/16/2026, 10:46:29 PM
1class Solution:
2    def minWindow(self, s1: str, s2: str) -> str:
3        n = len(s1)
4        m = len(s2)
5        dp = [[1000000000] * (m + 1) for i in range(n + 1)]
6        dp[0][0] = 0
7        end = 0
8        length = n + 1
9        for i in range(1, n + 1):
10            dp[i][0] = 0
11            for j in range(1, m + 1):
12                dp[i][j] = 1 + (dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1]
13                                else dp[i - 1][j])
14            if dp[i][m] < length:
15                length = dp[i][m]
16                end = i
17        return "" if length > n else s1[end - length:end]