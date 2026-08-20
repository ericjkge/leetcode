# Last updated: 8/20/2026, 11:39:29 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4
5        if n == 1:
6            return nums[0]
7
8        dp = [0] * n
9        dp[n - 1], dp[n - 2] = nums[n - 1], max(nums[n - 2], nums[n - 1])
10
11        for i in range(n - 3, -1, -1):
12            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
13
14        return dp[0]