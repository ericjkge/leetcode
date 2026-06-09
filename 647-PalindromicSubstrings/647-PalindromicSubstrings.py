# Last updated: 6/8/2026, 8:34:57 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        self.counter = 0
4
5        def expand(i, j):
6            while i >= 0 and j < len(s) and s[i] == s[j]:
7                self.counter += 1
8                i -= 1
9                j += 1
10
11        for i in range(len(s)):
12            expand(i, i)
13            expand(i, i + 1)
14        
15        return self.counter
16            
17