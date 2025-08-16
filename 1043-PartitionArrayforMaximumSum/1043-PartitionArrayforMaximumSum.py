# Last updated: 8/16/2025, 11:27:19 PM
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            curMax = 0
            for j in range(1, min(k, i) + 1):
                curMax = max(curMax, arr[i - j])
                dp[i] = max(dp[i], curMax * j + dp[i - j])
        
        return dp[n]