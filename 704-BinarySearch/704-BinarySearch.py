# Last updated: 7/24/2025, 3:53:56 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1