# Last updated: 8/12/2025, 10:22:02 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(amount, index):
            if amount < 0 or index == len(coins):
                return 0

            if amount == 0:
                return 1
            
            return dp(amount - coins[index], index) + dp(amount, index + 1)

        return dp(amount, 0)