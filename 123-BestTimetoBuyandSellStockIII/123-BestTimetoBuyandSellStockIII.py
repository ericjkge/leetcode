# Last updated: 7/15/2026, 8:32:17 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        @cache
4        def dp(i, j, k): # index, remaining transactions, state
5            if i >= len(prices) or j == 0:
6                return 0
7            
8            if k is False:
9                return max(-prices[i] + dp(i + 1, j, True), dp(i + 1, j, False))
10            else:
11                return max(prices[i] + dp(i + 1, j - 1, False), dp(i + 1, j, True))
12
13        return dp(0, 2, False)