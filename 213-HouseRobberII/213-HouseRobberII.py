# Last updated: 2/7/2026, 1:39:08 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5        
6        @cache
7        def dp(i, j):
8            if i >= j:
9                return 0
10            
11            return max(nums[i] + dp(i + 2, j), dp(i + 1, j))
12
13        return max(dp(0, len(nums) - 1), dp(1, len(nums)))