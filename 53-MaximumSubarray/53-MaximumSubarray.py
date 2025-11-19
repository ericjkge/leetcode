# Last updated: 11/19/2025, 11:19:27 AM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = min_prefix = 0
        best = -float("inf")

        for i in range(len(nums)):
            prefix += nums[i]
            best = max(best, prefix - min_prefix)
            min_prefix = min(prefix, min_prefix)
        
        return best