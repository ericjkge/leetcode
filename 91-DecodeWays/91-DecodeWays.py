# Last updated: 8/9/2026, 12:31:19 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        @cache
4        def dp(i):
5            if i == len(s):
6                return 1
7            
8            if s[i] == "0":
9                return 0
10            
11            total = dp(i + 1) # single letter
12            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and int(s[i + 1]) < 7):
13                total += dp(i + 2)
14            return total
15        
16        return dp(0)