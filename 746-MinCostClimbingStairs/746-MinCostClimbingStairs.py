# Last updated: 8/20/2026, 11:19:01 PM
1class Solution:
2    def minCostClimbingStairs(self, cost: List[int]) -> int:
3        n = len(cost)
4        dp = [0] * (n + 1)
5
6        for i in range(2, n + 1):
7            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
8
9        return dp[n]