# Last updated: 12/28/2025, 10:15:29 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        if n == 1:
6            return nums[0]
7
8        @cache
9        def dp(i, j):
10            if i >= j:
11                return 0
12            
13            return max(nums[i] + dp(i + 2, j), dp(i + 1, j))
14        
15        return max(dp(0, n - 1), dp(1, n))