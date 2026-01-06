# Last updated: 1/6/2026, 9:56:50 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        @cache
4        def dp(i):
5            if i == 0:
6                return 0
7
8            if i < 0:
9                return float("inf")
10
11            best = float("inf")
12            for coin in coins:
13                best = min(best, dp(i - coin) + 1)
14            return best
15
16        return dp(amount) if dp(amount) != float("inf") else -1