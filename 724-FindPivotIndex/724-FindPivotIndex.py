# Last updated: 7/4/2025, 12:35:40 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] + nums[i])

        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]

        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 0
            right = suffix[i + 1] if i + 1 < len(nums) else 0
            if left == right:
                return i
        
        return -1