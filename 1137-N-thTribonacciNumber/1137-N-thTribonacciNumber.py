# Last updated: 8/19/2026, 10:30:35 AM
1class Solution:
2    def tribonacci(self, n: int) -> int:
3        if n < 1:
4            return 0
5        
6        if n < 3:
7            return 1
8
9        dp = [0 for _ in range(n + 1)]
10        dp[0], dp[1], dp[2] = 0, 1, 1
11
12        for i in range(3, n + 1):
13            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
14        
15        return dp[n]