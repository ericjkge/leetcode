# Last updated: 2/8/2026, 4:53:49 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        @cache
4        def dp(i, j):
5            if i == len(text1) or j == len(text2):
6                return 0
7            
8            if text1[i] == text2[j]:
9                return 1 + dp(i + 1, j + 1)
10            
11            return max(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
12        
13        return dp(0, 0)