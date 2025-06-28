# Last updated: 6/28/2025, 3:31:54 PM
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(i):
            if i < 0:
                return float("inf")
            if i == 0:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = min(dp(i - coin) + 1 for coin in coins)
            return memo[i]
            
        ans = dp(amount)
        return ans if ans != float("inf") else -1