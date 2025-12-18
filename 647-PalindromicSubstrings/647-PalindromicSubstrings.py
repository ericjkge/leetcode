# Last updated: 12/17/2025, 10:08:29 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        n = len(s)
4        self.ans = 0
5
6        def expand(l, r):
7            while l >= 0 and r < n and s[l] == s[r]:
8                self.ans += 1
9                l -= 1
10                r += 1
11        
12        for i in range(n):
13            expand(i, i)
14            expand(i, i + 1)
15        
16        return self.ans