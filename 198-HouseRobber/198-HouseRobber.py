# Last updated: 8/14/2025, 3:16:26 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, n):
            dp.append(max(dp[i - 2] + nums[i], dp[i - 1]))

        return dp[n - 1]