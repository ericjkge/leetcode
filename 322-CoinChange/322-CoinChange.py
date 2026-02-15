# Last updated: 2/15/2026, 12:34:27 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        @cache
4        def dp(i):
5            if i > amount:
6                return float("inf")
7            
8            if i == amount:
9                return 0
10        
11            fewest = float("inf")
12            for coin in coins:
13                fewest = min(fewest, 1 + dp(i + coin))
14            return fewest
15
16        return dp(0) if dp(0) != float("inf") else -1