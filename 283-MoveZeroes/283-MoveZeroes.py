# Last updated: 7/3/2025, 10:15:44 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tracker = pointer = 0
        while pointer < len(nums):
            if nums[pointer] != 0:
                nums[pointer], nums[tracker] = nums[tracker], nums[pointer]
                tracker += 1
            pointer += 1