# Last updated: 8/19/2025, 10:43:51 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dp(i, j):
            if i == 0 and j < 0:
                return 1
            if j < 0:
                return 0
            
            return dp(i - nums[j], j - 1) + dp(i + nums[j], j - 1)
        
        return dp(target, n - 1)