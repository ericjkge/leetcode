# Last updated: 11/6/2026, 6:26:34 PM
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