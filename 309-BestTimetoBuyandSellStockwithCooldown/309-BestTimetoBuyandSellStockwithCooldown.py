# Last updated: 1/2/2026, 9:50:12 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        @cache
4        def dp(i, state): # 0 for resting, 1 for holding, 2 for cooldown
5            if i == len(prices):
6                return 0
7            
8            if state == 0:
9                return max(-prices[i] + dp(i + 1, 1), dp(i + 1, 0))
10            elif state == 1:
11                return max(prices[i] + dp(i + 1, 2), dp(i + 1, 1))
12            else:
13                return dp(i + 1, 0)
14
15        return dp(0, 0)