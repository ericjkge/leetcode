# Last updated: 12/29/2025, 8:08:38 PM
1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        m, n = len(text1), len(text2)
4
5        @cache
6        def dp(i, j):
7            if i == m or j == n:
8                return 0
9            elif text1[i] == text2[j]:
10                return 1 + dp(i + 1, j + 1)
11            else:
12                return max(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1))
13
14        return dp(0, 0)
15