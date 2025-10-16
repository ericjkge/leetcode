# Last updated: 10/16/2025, 11:09:52 AM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(i):
            if i >= n:
                return 0
            
            return cost[i] + min(dp(i + 1), dp(i + 2))
            
        return min(dp(0), dp(1))