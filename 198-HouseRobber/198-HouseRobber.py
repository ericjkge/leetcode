# Last updated: 12/26/2025, 10:57:52 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        @cache
6        def dp(i):
7            if i >= n:
8                return 0
9            
10            return max(nums[i] + dp(i + 2), dp(i + 1))
11        
12        return dp(0)