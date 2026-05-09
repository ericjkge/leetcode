# Last updated: 5/9/2026, 10:13:33 AM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        @cache
4        def dp(i, j):
5            if i == len(nums) and j == target:
6                return 1
7            
8            if i == len(nums):
9                return 0
10            
11            return dp(i + 1, j - nums[i]) + dp(i + 1, j + nums[i])
12        
13        return dp(0, 0)