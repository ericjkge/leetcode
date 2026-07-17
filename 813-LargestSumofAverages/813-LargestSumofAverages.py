# Last updated: 7/17/2026, 10:31:58 AM
1class Solution:
2    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
3        n = len(nums)
4
5        @cache
6        def dp(i, j):
7            if j == 1:
8                return sum(nums[i:n]) / len(nums[i:n])
9            
10            mx = 0
11            for index in range(i, n - j + 1):
12                mx = max(mx, sum(nums[i:index + 1]) / len(nums[i:index + 1]) + dp(index + 1, j - 1))
13            return mx
14
15        return dp(0, k)