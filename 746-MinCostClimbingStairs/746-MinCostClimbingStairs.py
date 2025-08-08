# Last updated: 8/8/2025, 10:59:15 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return 0
            return min(dp(i - 2) + cost[i - 2], dp(i - 1) + cost[i - 1])
        
        return dp(len(cost))