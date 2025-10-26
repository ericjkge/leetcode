# Last updated: 10/26/2025, 12:17:40 AM
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        target = prefix[-1] / 2

        return sum(1 for i in range(len(nums) - 1) if prefix[i] >= prefix[-1] - prefix[i])