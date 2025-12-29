# Last updated: 12/29/2025, 8:51:23 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4
5        @cache
6        def dp(i):
7            if i == 0 or i == 1:
8                return 0
9            
10            return min(cost[i - 1] + dp(i - 1), cost[i - 2] + dp(i - 2))
11        
12        return dp(n)