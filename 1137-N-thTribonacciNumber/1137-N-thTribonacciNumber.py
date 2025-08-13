# Last updated: 8/13/2025, 11:56:41 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
        
        return dp[n]