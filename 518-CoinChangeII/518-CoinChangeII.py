# Last updated: 9/5/2025, 9:57:30 AM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @cache
        def dp(i, rem): # ways to get rem with coins[:i]
            if rem == 0:
                return 1
            if rem < 0 or i == n:
                return 0
            return dp(i + 1, rem) + dp(i, rem - coins[i])

        return dp(0, amount)

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