# Last updated: 8/15/2025, 7:57:01 PM
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @cache
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, n - 1)