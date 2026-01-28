# Last updated: 1/28/2026, 9:16:26 AM
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
11            if i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j):
12                return True
13                
14            if j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1):
15                return True
16
17            return False
18
19        return dp(0, 0)