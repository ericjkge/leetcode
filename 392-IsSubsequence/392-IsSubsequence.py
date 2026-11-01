# Last updated: 11/1/2026, 11:26:53 AM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i = j = 0
4
5        while i < len(s) and j < len(t):
6            if s[i] == t[j]:
7                i += 1
8                j += 1
9            else:
10                j += 1
11
12        return i == len(s)
13