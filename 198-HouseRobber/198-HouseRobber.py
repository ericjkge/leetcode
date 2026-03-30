# Last updated: 3/30/2026, 9:24:26 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        @cache
4        def dp(i):
5            if i >= len(nums):
6                return 0
7            
8            return max(nums[i] + dp(i + 2), dp(i + 1))
9        
10        return dp(0)