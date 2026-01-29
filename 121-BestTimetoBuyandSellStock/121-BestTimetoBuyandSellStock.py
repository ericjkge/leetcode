# Last updated: 1/29/2026, 10:46:23 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = float("inf")
4        max_profit = float("-inf")
5
6        for price in prices:
7            min_price = min(min_price, price)
8            max_profit = max(max_profit, price - min_price)
9
10        return max_profit