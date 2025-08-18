# Last updated: 8/18/2025, 10:51:36 PM
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        a, b = len(s), len(t)
        
        @cache
        def dp(i, j):
            if i == a and j == b:
                return 1

            if i == a:
                return 0
            if j == b:
                return 1
                
            if s[i] == t[j]:
                return dp(i + 1, j + 1) + dp(i + 1, j)
            return dp(i + 1, j)
        
        return dp(0, 0)