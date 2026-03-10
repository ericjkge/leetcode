# Last updated: 3/10/2026, 7:28:08 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        if len(s1) + len(s2) != len(s3):
4            return False
5
6        @cache
7        def dp(i, j):
8            if i + j == len(s3):
9                return True
10            
11            if (i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j)) or (j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1)):
12                return True
13
14            return False
15        
16        return dp(0, 0)
17        