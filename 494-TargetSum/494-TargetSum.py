# Last updated: 8/19/2025, 10:45:07 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dp(i, j):
            if i == target and j == n:
                return 1
            if j == n:
                return 0

            return dp(i - nums[j], j + 1) + dp(i + nums[j], j + 1)
        
        return dp(0, 0)