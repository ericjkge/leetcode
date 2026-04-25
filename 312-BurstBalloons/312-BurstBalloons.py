# Last updated: 4/24/2026, 11:13:22 PM
1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        arr = [1] + nums + [1]
4
5        @cache
6        def dp(i, j):
7            if i + 1 == j:
8                return 0
9            
10            coins = 0
11            for k in range(i + 1, j):
12                coins = max(coins, arr[i] * arr[k] * arr[j] + dp(i, k) + dp(k, j))
13
14            return coins
15
16        return dp(0, len(arr) - 1)