# Last updated: 7/5/2026, 11:42:00 PM
1class Solution:
2    def minCut(self, s: str) -> int:
3        @cache
4        def dp(i):
5            if i == len(s):
6                return 0
7
8            count = float("inf")
9            for j in range(i + 1, len(s) + 1):
10                substring = s[i:j]
11                if substring == substring[::-1]:
12                    count = min(count, 1 + dp(j))
13
14            return count
15        
16        return dp(0) - 1