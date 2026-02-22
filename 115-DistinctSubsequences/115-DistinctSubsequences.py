# Last updated: 2/22/2026, 12:22:12 PM
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
11            if s[i] == t[j]:
12                return dp(i + 1, j + 1) + dp(i + 1, j)
13
14            return dp(i + 1, j)
15        
16        return dp(0, 0)