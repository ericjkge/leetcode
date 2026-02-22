# Last updated: 2/22/2026, 9:03:12 AM
1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        arr = [1] + nums + [1]
4        n = len(arr)
5
6        @cache
7        def dp(i, j):
8            if i + 1 == j:
9                return 0
10            
11            best = 0
12            for k in range(i + 1, j):
13                best = max(best, arr[i] * arr[j] * arr[k] + dp(i, k) + dp(k, j))
14            return best
15
16        return dp(0, n - 1)
17