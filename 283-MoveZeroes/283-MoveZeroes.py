# Last updated: 7/8/2025, 9:34:04 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = 0
        for pointer in range(len(nums)):
            if nums[pointer] != 0:
                nums[tracker], nums[pointer] = nums[pointer], nums[tracker]
                tracker += 1
