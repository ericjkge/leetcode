# Last updated: 4/24/2026, 10:17:05 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        @cache
4        def dp(i, j): # j = 0 (nothing), 1 (holding), 2 (cooldown)
5            if i == len(prices):
6                return 0
7
8            if j == 0:
9                return max(dp(i + 1, 0), -prices[i] + dp(i + 1, 1))
10            elif j == 1:
11                return max(dp(i + 1, 1), prices[i] + dp(i + 1, 2))
12            else:
13                return dp(i + 1, 0)
14        
15        return dp(0, 0)