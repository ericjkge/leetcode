# Last updated: 3/20/2026, 3:19:17 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        lowest = float("inf")
4        profit = 0
5
6        for price in prices:
7            lowest = min(lowest, price)
8            profit = max(profit, price - lowest)
9        
10        return profit