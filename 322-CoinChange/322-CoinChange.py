# Last updated: 2/15/2026, 9:33:16 AM
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
11            fewest = float("inf")
12            for k in range(i, len(coins)):
13                fewest = min(fewest, 1 + dp(k, j + coins[k]))
14            
15            return fewest
16
17        ans = dp(0, 0)
18        return ans if ans != float("inf") else -1