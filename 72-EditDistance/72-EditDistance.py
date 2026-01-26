# Last updated: 1/26/2026, 9:07:27 AM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m, n = len(word1), len(word2)
4        
5        @cache
6        def dp(i, j):
7            if i == m and j == n:
8                return 0 # Done
9            
10            if i == m:
11                return n - j # All inserts
12            
13            if j == n:
14                return m - i # All deletes
15            
16            if word1[i] == word2[j]:
17                return dp(i + 1, j + 1)
18            
19            return 1 + min(dp(i + 1, j), dp(i, j + 1), dp(i + 1, j + 1)) # Delete, insert, replace
20
21        return dp(0, 0)