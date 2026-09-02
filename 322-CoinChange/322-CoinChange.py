# Last updated: 9/2/2026, 1:48:24 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        @cache
4        def dp(i, j):
5            if j == amount:
6                return 0
7
8            if j > amount or i == len(coins):
9                return float("inf")
10            
11            return min(1 + dp(i, j + coins[i]), dp(i + 1, j))
12        
13        res = dp(0, 0)
14        return res if res != float("inf") else -1