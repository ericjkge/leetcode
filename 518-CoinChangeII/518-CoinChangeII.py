# Last updated: 10/1/2025, 9:48:46 AM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @cache
        def dp(i, j):
            if i == 0:
                return 1
            if i < 0 or j == n:
                return 0
            return dp(i - coins[j], j) + dp(i, j + 1)
        
        return dp(amount, 0)

        # Alternative: 
        # self.ans = 0
        # n = len(coins)

        # def backtrack(index, total):
        #     if total > amount:
        #         return

        #     if total == amount:
        #         self.ans += 1
        #         return
            
        #     for i in range(index, n):
        #         backtrack(i, total + coins[i])
        
        # backtrack(0, 0)
        # return self.ans