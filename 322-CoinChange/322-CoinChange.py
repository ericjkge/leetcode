# Last updated: 7/5/2026, 8:34:00 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        @cache
4        def dp(i, j):
5            if i >= len(coins) or j > amount:
6                return float("inf")
7            
8            if j == amount:
9                return 0
10
11            return min(1 + dp(i, j + coins[i]), dp(i + 1, j))
12        
13        res = dp(0, 0)
14        return res if res != float("inf") else -1