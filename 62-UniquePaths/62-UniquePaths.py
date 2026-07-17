# Last updated: 7/17/2026, 9:55:31 AM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        @cache
4        def dp(i, j):
5            if i == m - 1 or j == n - 1:
6                return 1
7            
8            return dp(i + 1, j) + dp(i, j + 1)
9        
10        return dp(0, 0)