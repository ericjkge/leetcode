# Last updated: 11/30/2025, 10:06:53 AM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        if len(s1) + len(s2) != len(s3):
4            return False
5
6        a, b, c = len(s1), len(s2), len(s3)
7
8        @cache
9        def dp(i, j):
10            if i == a and j == b:
11                return True
12
13            if i < a and s1[i] == s3[i + j] and dp(i + 1, j):
14                return True
15            
16            if j < b and s2[j] == s3[i + j] and dp(i, j + 1):
17                return True
18            
19            return False
20        
21        return dp(0, 0)