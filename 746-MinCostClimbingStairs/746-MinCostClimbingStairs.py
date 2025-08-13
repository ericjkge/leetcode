# Last updated: 8/14/2025, 12:19:08 AM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]
        for i in range(2, len(cost) + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))

        return dp[len(cost)]