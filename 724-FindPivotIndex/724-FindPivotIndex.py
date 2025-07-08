# Last updated: 7/8/2025, 9:55:38 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        suffix = [0] * len(nums)

        for i in range(len(nums)):
            if i > 0:
                prefix.append(prefix[-1] + nums[i])
            else:
                prefix.append(nums[i])
    
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = suffix[i + 1] + nums[i]
        
        # handle edges
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 0
            right = suffix[i + 1] if i < len(nums) - 1 else 0
            if left == right:
                return i
        return -1