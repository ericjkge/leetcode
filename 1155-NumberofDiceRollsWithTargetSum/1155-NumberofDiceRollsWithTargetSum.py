# Last updated: 7/22/2025, 5:03:57 PM
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(i, j): # No. of ways to get i using j rolls
            if (i <= 0 and j != 0) or (i != 0 and j == 0):
                return 0

            if i == 0 and j == 0:
                return 1

            ways = 0
            for val in range(1, k + 1):
                ways += dp(i - val, j - 1)

            return ways % MOD

        return dp(target, n)