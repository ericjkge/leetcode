# Last updated: 1/9/2026, 10:27:19 AM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4
5        @cache
6        def dp(i, j):
7            if i == n and j == target:
8                return 1
9            
10            if i == n and j != target:
11                return 0
12
13            return dp(i + 1, j - nums[i]) + dp(i + 1, j + nums[i])
14
15        return dp(0, 0)