# Last updated: 2/19/2026, 9:25:47 AM
1class Solution:
2    def findTargetSumWays(self, nums: List[int], target: int) -> int:
3        @cache
4        def dp(i, j):
5            if i == len(nums):
6                if j == target:
7                    return 1
8                return 0
9            
10            return dp(i + 1, j + nums[i]) + dp(i + 1, j - nums[i])
11        
12        return dp(0, 0)
13