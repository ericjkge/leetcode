# Last updated: 5/12/2026, 9:36:09 AM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        @cache
4        def dp(i, j):
5            if j == len(p):
6                return i == len(s)
7
8            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
9            if j + 1 < len(p) and p[j + 1] == "*":
10                return dp(i, j + 2) or (match and dp(i + 1, j))
11            
12            return match and dp(i + 1, j + 1)
13        
14        return dp(0, 0)