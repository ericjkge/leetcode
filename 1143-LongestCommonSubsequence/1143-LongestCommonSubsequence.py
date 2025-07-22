# Last updated: 7/22/2025, 3:22:30 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)