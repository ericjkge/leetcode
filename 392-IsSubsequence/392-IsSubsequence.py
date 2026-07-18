# Last updated: 7/17/2026, 8:18:58 PM
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        p1 = p2 = 0
4
5        while p1 < len(s):
6            if p2 == len(t):
7                return False
8            
9            if s[p1] == t[p2]:
10                p1 += 1
11                p2 += 1
12            else:
13                p2 += 1
14            
15        return True
16