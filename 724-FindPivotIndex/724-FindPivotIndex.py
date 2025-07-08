# Last updated: 7/8/2025, 9:52:24 AM
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
        if len(nums) == 1:
            return 0
     

        if suffix[1] == 0:
            return 0

        for i in range(1, len(nums) - 1):
            if prefix[i - 1] == suffix[i + 1]:
                return i
        
        if prefix[len(nums) - 2] == 0:
            return len(nums) - 1

        return -1
