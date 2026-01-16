# Last updated: 1/16/2026, 10:46:04 PM
1class Solution:
2    def minWindow(self, s1: str, s2: str) -> str:
3        n = len(s1)
4        m = len(s2)
5        # declare the DP table and initialize it with large values
6        dp = [[1000000000] * (m + 1) for i in range(n + 1)]
7        # the base case of DP
8        dp[0][0] = 0
9        end = 0
10        length = n + 1
11        for i in range(1, n + 1):
12            # the base case of DP
13            dp[i][0] = 0
14            # DP transitions
15            for j in range(1, m + 1):
16                # different transitions depending on whether s1[i-1] == s2[j-1]
17                dp[i][j] = 1 + (dp[i - 1][j - 1] if s1[i - 1] == s2[j - 1]
18                                else dp[i - 1][j])
19            # update the answer
20            if dp[i][m] < length:
21                length = dp[i][m]
22                end = i
23        # return the answer
24        return "" if length > n else s1[end - length:end]