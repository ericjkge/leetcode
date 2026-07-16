# Last updated: 7/15/2026, 8:12:37 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        ans = 0
4
5        for i in range(len(prices)):
6            if i > 0 and prices[i] > prices[i - 1]:
7                ans += prices[i] - prices[i - 1]
8        
9        return ans