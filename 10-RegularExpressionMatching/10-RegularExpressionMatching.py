# Last updated: 11/24/2025, 9:34:18 AM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            
            first = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                return dp(i, j + 2) or (first and dp(i + 1, j))

            return first and dp(i + 1, j + 1)
        
        return dp(0, 0)