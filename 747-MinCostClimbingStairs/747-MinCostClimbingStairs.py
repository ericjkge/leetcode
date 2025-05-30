# Last updated: 5/30/2025, 2:50:58 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dp(i):
            if i == 0 or i == 1:
                return 0
            
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            
        return dp(len(cost))