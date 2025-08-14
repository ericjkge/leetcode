# Last updated: 8/15/2025, 12:32:47 AM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a, b = len(text1), len(text2)

        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i - 1, j - 1)
            return max(dp(i - 1, j), dp(i, j - 1))
        
        return dp(a - 1, b - 1)