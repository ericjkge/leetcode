# Last updated: 8/19/2025, 9:53:56 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(i): # min coins for amount i
            if i == 0:
                return 0
            if i < 0:
                return float("inf")

            ans = float("inf")
            for coin in coins:
                ans = min(ans, 1 + dp(i - coin))
            
            return ans

        return dp(amount) if dp(amount) != float("inf") else -1
        