# Last updated: 8/8/2025, 11:23:31 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 0
                
            if i < 0:
                return float("inf")

            return min(dp(i - c) for c in coins) + 1
        
        ans = dp(amount)
        return ans if ans != float("inf") else -1