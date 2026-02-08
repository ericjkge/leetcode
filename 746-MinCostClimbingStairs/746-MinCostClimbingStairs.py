# Last updated: 2/8/2026, 4:52:06 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        @cache
4        def dp(i):
5            if i >= len(cost):
6                return 0
7
8            return cost[i] + min(dp(i + 1), dp (i + 2))
9        
10        return min(dp(0), dp(1))