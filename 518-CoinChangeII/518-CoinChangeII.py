# Last updated: 8/18/2025, 12:18:13 AM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        self.ans = 0
        
        memo = {}
        def dp(remain, start):
            if remain == 0:
                return 1
            if remain < 0 or start == n:
                return 0
            
            if (remain, start) in memo:
                return memo[(remain, start)]
            
            memo[(remain, start)] = dp(remain - coins[start], start) + dp(remain, start + 1)
            return memo[(remain, start)]

        return dp(amount, 0)