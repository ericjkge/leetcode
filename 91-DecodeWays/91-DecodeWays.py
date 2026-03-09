# Last updated: 3/9/2026, 1:52:18 PM
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
11            ways = dp(i + 1)
12
13            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i + 1]) <= 6)):
14                ways += dp(i + 2)
15            
16            return ways
17        
18        return dp(0)