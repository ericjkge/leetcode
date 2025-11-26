# Last updated: 11/25/2025, 7:16:48 PM
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