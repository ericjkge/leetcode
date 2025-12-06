# Last updated: 12/6/2025, 10:20:31 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = prices[0]
4        max_profit = 0
5
6        for price in prices:
7            min_price = min(min_price, price)
8            max_profit = max(price - min_price, max_profit)
9
10        return max_profit