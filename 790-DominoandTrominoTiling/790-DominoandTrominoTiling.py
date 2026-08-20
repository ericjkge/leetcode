# Last updated: 8/20/2026, 11:52:37 PM
1class Solution:
2    def numTilings(self, n: int) -> int:
3        MOD = 10 ** 9 + 7
4        
5        @cache
6        def dp(i):
7            if i == 1:
8                return 1
9            elif i == 2:
10                return 2
11            elif i == 3:
12                return 5
13
14            return dp(i - 1) * 2 + dp(i - 3)
15
16        return dp(n) % MOD