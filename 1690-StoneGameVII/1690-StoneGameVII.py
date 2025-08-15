# Last updated: 8/15/2025, 9:26:02 PM
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0, stones[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + stones[i])

        def getSum(i, j):
            return prefix[j + 1] - prefix[i]
            

        dp = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                takeL = getSum(l + 1, r) - dp[l + 1][r]
                takeR = getSum(l, r - 1) - dp[l][r - 1]
                dp[l][r] = max(takeL, takeR)
        
        return dp[0][n - 1]