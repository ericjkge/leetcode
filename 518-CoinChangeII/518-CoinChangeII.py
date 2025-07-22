# Last updated: 7/22/2025, 2:12:45 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        @cache
        def dp(i, j): # No. of ways to make up i using coins[j:]
            if i == 0:
                return 1
            
            total = 0
            for index in range(j, n):
                if coins[index] <= i:
                    total += dp(i - coins[index], index)
            
            return total
        
        return dp(amount, 0)