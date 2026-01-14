# Last updated: 1/14/2026, 11:19:33 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        n = len(coins)
4        
5        @cache
6        def dp(i, j): # index, amount
7            if j > amount or i == n:
8                return 0
9            
10            if j == amount:
11                return 1
12
13            return dp(i, j + coins[i]) + dp(i + 1, j)
14
15        return dp(0, 0)