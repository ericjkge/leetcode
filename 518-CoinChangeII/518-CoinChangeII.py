# Last updated: 8/19/2025, 10:18:08 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @cache
        def dp(i, j):
            if i < 0 or j == n:
                return 0
            if i == 0:
                return 1
            
            return dp(i - coins[j], j) + dp(i, j + 1)

        return dp(amount, 0)