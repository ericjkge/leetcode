# Last updated: 11/13/2026, 1:50:07 AM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m, n = len(word1), len(word2)
4
5        @cache
6        def dp(i, j):
7            if i == m and j == n:
8                return 0
9            
10            if i == m:
11                return n - j
12            
13            if j == n:
14                return m - i
15            
16            if word1[i] == word2[j]:
17                return dp(i + 1, j + 1)
18                
19            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1))
20        
21        return dp(0, 0)