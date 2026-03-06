# Last updated: 3/6/2026, 11:59:40 AM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        @cache
4        def dp(i):
5            if i == n:
6                return 1
7            
8            if i > n:
9                return 0
10
11            return dp(i + 1) + dp(i + 2)
12        
13        return dp(0)