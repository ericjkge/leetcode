# Last updated: 5/31/2025, 3:27:18 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, state): # 0 for resting, 1 for holding, 2 for cooldown
            if i == len(prices):
                return 0

            if state == 0:
                return max(dp(i+1, 0), -prices[i] + dp(i+1, 1))
            elif state == 1:
                return max(dp(i+1, 1), prices[i] + dp(i+1, 2))
            else:
                return dp(i+1, 0)
        
        return dp(0, 0)