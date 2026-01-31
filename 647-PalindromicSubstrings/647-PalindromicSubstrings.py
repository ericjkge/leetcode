# Last updated: 1/31/2026, 1:18:10 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        self.ans = 0
5
6        def expand(i, j):
7            while i >= 0 and j < n and s[i] == s[j]:
8                self.ans += 1
9                i -= 1
10                j += 1
11                
12        for k in range(n):
13            expand(k, k)
14            expand(k, k + 1)
15
16        return self.ans