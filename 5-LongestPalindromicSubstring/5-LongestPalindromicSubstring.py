# Last updated: 6/6/2026, 12:27:12 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        def expand(i, j):
4            while i > 0 and j < len(s) - 1 and s[i] == s[j]:
5                i -= 1
6                j += 1
7            
8            if j < len(s) and s[i] == s[j]:
9                return i, j
10            return i + 1, j - 1
11        
12        longest = ""
13        for i in range(len(s)):
14            ei, ej = expand(i, i + 1)
15            if ej - ei + 1 > len(longest):
16                longest = s[ei:ej + 1]
17            oi, oj = expand(i, i)
18            if oj - oi + 1 > len(longest):
19                longest = s[oi:oj + 1]
20            
21        return longest