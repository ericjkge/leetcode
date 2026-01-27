# Last updated: 1/27/2026, 12:03:00 PM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        @cache
4        def dp(i):
5            if i == len(s):
6                return 1
7
8            if int(s[i]) == 0:
9                return 0
10            
11            ways = dp(i + 1)
12            if i + 1 < len(s) and (int(s[i]) == 1 or (int(s[i]) == 2 and 0 <= int(s[i + 1]) <= 6)):
13                ways += dp(i + 2)
14            return ways
15
16        return dp(0)