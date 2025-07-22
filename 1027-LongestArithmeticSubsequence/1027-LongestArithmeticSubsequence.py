# Last updated: 7/22/2025, 9:24:29 PM
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}

        for right in range(len(nums)):
            for left in range(right):
                dp[(right, nums[right] - nums[left])] = dp.get((left, nums[right] - nums[left]), 1) + 1
        
        return max(dp.values())