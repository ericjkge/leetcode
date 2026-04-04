# Last updated: 4/4/2026, 9:34:16 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return nums[0]
5
6
7        @cache
8        def dp(i):
9            if i >= len(nums) - 1:
10                return 0
11            
12            return max(nums[i] + dp(i + 2), dp(i + 1))
13        
14        @cache
15        def dp2(i):
16            if i >= len(nums):
17                return 0
18            
19            return max(nums[i] + dp2(i + 2), dp2(i + 1))
20        
21
22        return max(dp(0), dp2(1))