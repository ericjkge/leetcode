# Last updated: 11/24/2025, 9:21:12 AM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)

        @cache
        def dp(i, j): # s[i:] matches p[j:]
            if j == len(p):
                return i == len(s)

            first = (i < len(s) and (s[i] == p[j] or p[j] == "."))

            if j + 1 < len(p) and p[j + 1] == "*":
                return dp(i, j + 2) or (first and dp(i + 1, j)) # Use * 0 times or 1 time

            return first and dp(i + 1, j + 1)
            
        return dp(0, 0)