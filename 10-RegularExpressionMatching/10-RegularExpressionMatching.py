# Last updated: 5/11/2026, 10:05:01 AM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        @cache
4        def dp(i, j):
5            if j == len(p):
6                return i == len(s)
7            
8            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
9
10            if j + 1 < len(p) and p[j + 1] == "*":
11                return dp(i, j + 2) or (match and dp(i + 1, j))
12
13            return match and dp(i + 1, j + 1)
14
15        return dp(0, 0)