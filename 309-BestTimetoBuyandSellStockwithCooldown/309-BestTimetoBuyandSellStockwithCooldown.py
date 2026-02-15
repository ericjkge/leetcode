# Last updated: 2/15/2026, 1:03:54 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        @cache
4        def dp(i, j): # day, status (0 resting, 1 holding, 2 cooldown)
5            if i == len(prices):
6                return 0
7
8            if j == 0:
9                return max(dp(i + 1, 0), -prices[i] + dp(i + 1, 1))
10            
11            if j == 1:
12                return max(prices[i] + dp(i + 1, 2), dp(i + 1, 1))
13            
14            return dp(i + 1, 0)
15
16        return max(dp(i, 0) for i in range(len(prices)))