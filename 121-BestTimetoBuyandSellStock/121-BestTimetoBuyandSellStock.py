# Last updated: 7/15/2026, 8:10:26 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        mx = 0
4        lowest = float("inf")
5
6        for price in prices:
7            lowest = min(lowest, price)
8            mx = max(mx, price - lowest)
9        
10        return mx
11            