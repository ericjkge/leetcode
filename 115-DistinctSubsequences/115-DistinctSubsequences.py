# Last updated: 3/20/2026, 3:15:52 PM
1class Solution:
2    def numDistinct(self, s: str, t: str) -> int:
3        @cache
4        def dp(i, j):
5            if j == len(t):
6                return 1
7            
8            if i == len(s):
9                return 0
10
11            ways = 0
12            
13            if s[i] == t[j]:
14                ways += dp(i + 1, j + 1)
15            
16            ways += dp(i + 1, j)
17
18            return ways
19        
20        return dp(0, 0)