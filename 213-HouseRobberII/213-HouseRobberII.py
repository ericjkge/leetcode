# Last updated: 12/28/2025, 10:17:13 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        if n == 1:
5            return nums[0]
6
7        @cache
8        def dp(i, j):
9            if i >= j:
10                return 0
11            
12            return max(nums[i] + dp(i + 2, j), dp(i + 1, j))
13        
14        return max(dp(0, n - 1), dp(1, n))