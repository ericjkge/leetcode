# Last updated: 8/21/2026, 3:11:51 PM
1class Solution:
2    def maxProfit(self, prices: List[int], fee: int) -> int:
3        @cache
4        def dp(i, j):
5            if i == len(prices):
6                return 0
7            
8            if j == 0:
9                return max(dp(i + 1, 1) - prices[i], dp(i + 1, 0))
10            else:
11                return max(dp(i + 1, 0) - fee + prices[i], dp(i + 1, 1))
12            
13        return dp(0, 0)