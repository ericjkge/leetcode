# Last updated: 9/25/2025, 9:47:37 AM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, it, right = 0, 0, len(nums) - 1

        while it <= right:
            if nums[it] == 2:
                nums[it], nums[right] = nums[right], nums[it]
                right -= 1
            elif nums[it] == 0:
                nums[it], nums[left] = nums[left], nums[it]
                left += 1
                it += 1
            else:
                it += 1