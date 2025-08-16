# Last updated: 8/16/2025, 9:00:12 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return dp(i + 1, j - 1) # Check smaller palindromic substring

        ans = 0
        for i in range(n):
            for j in range(i, n):
                ans += dp(i, j)

        return ans