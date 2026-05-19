# Last updated: 5/19/2026, 10:18:11 AM
1class Solution:
2    def maxCoins(self, nums: List[int]) -> int:
3        nums = [1] + nums + [1]
4
5        @cache
6        def dp(i, j):
7            if i + 1 == j:
8                return 0
9            
10            mx = 0
11            for k in range(i + 1, j):
12                mx = max(mx, dp(i, k) + nums[i] * nums[k] * nums[j] + dp(k, j))
13            return mx
14        
15        return dp(0, len(nums) - 1)