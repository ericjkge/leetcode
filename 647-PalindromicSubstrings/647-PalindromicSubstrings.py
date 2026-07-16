# Last updated: 7/15/2026, 9:05:26 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        @cache
4        def dp(i, j):
5            if j - i < 1:
6                return True
7            return s[i] == s[j] and dp(i + 1, j - 1)
8        
9        return sum(dp(i, j) for i in range(len(s)) for j in range(i, len(s)))