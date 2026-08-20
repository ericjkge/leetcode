# Last updated: 8/20/2026, 7:32:19 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        # dp = [0] * len(cost)
4        # dp[0] = dp[1] = 0
5
6        # for i in range(2, len(cost)):
7        
8
9
10        @cache
11        def dp(i):
12            if i >= len(cost):
13                return 0
14            
15            return cost[i] + min(dp(i + 1), dp(i + 2))
16
17        return min(dp(0), dp(1))