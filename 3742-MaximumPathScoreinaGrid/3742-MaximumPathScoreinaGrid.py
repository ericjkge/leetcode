# Last updated: 5/29/2026, 6:09:04 PM
1class Solution:
2    def maxPathScore(self, grid, k):
3        m, n = len(grid), len(grid[0])
4
5        INF = float("-inf")
6        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
7        dp[0][0][0] = 0
8
9        for i in range(m):
10            for j in range(n):
11                for c in range(k + 1):
12                    if dp[i][j][c] == INF:
13                        continue
14
15                    if i + 1 < m:
16                        val = grid[i + 1][j]
17                        cost = 0 if val == 0 else 1
18                        if c + cost <= k:
19                            dp[i + 1][j][c + cost] = max(
20                                dp[i + 1][j][c + cost], dp[i][j][c] + val
21                            )
22
23                    if j + 1 < n:
24                        val = grid[i][j + 1]
25                        cost = 0 if val == 0 else 1
26                        if c + cost <= k:
27                            dp[i][j + 1][c + cost] = max(
28                                dp[i][j + 1][c + cost], dp[i][j][c] + val
29                            )
30
31        ans = max(dp[m - 1][n - 1])
32        return -1 if ans < 0 else ans
33