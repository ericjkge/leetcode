# Last updated: 3/6/2026, 11:49:58 AM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        @cache
4        def dp(i, j):
5            if i == m - 1 and j == n - 1:
6                return 1
7            
8            if i > m - 1 or j > n - 1:
9                return 0
10
11            return dp(i + 1, j) + dp(i, j + 1)
12        
13        return dp(0, 0)