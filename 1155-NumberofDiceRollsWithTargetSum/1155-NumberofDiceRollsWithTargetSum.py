# Last updated: 8/19/2025, 12:51:48 AM
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, j): # num ways to reach sum j with i dice
            if i == 0:
                return 1 if j == 0 else 0
            if j < 0:
                return 0

            ways = 0
            for num in range(1, k + 1):
                ways += dp(i - 1, j - num)
            return ways % MOD
        
        return dp(n, target)