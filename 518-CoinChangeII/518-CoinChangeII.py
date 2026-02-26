# Last updated: 2/26/2026, 9:51:19 AM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        @cache
4        def dp(i, j): # index, total
5            if j == amount:
6                return 1
7            
8            if i == len(coins) or j > amount:
9                return 0
10            
11            return dp(i, j + coins[i]) + dp(i + 1, j)
12        
13        return dp(0, 0)
14