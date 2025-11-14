# Last updated: 11/14/2025, 1:01:00 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid
            else:
                right = mid
        
        return min(nums[left], nums[right])