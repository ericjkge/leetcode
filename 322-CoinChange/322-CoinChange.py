# Last updated: 7/5/2026, 8:39:00 PM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        memo = {}
4
5        def dp(i, j):
6            if (i, j) in memo:
7                return memo[(i, j)]
8
9            if i >= len(coins) or j > amount:
10                memo[(i, j)] = float("inf")
11                return memo[(i, j)]
12            
13            if j == amount:
14                memo[(i, j)] = 0
15                return memo[(i, j)]
16
17            memo[(i, j)] = min(1 + dp(i, j + coins[i]), dp(i + 1, j))
18            return memo[(i, j)]
19        
20        res = dp(0, 0)
21        return res if res != float("inf") else -1