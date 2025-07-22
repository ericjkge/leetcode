# Last updated: 7/22/2025, 2:45:51 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        
        for r in range(len(coins) + 1):
            dp[r][0] = 1
        
        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                target = c - coins[r - 1]
                if target < 0:
                    dp[r][c] = dp[r - 1][c]
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][target]
        
        return dp[-1][-1]