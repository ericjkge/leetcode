# Last updated: 5/30/2025, 12:07:40 PM
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n - 1
        output = [0] * n
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                output[i] = nums[left] * nums[left]
                left += 1
            else:
                output[i] = nums[right] * nums[right]
                right -= 1
        return output
            