# Last updated: 3/6/2026, 12:06:06 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        @cache
4        def dp(i, j):
5            if j == len(word2):
6                return len(word1) - i
7            
8            if i == len(word1):
9                return len(word2) - j
10
11            if word1[i] == word2[j]:
12                return dp(i + 1, j + 1)
13            
14            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
15        
16        return dp(0, 0)
17