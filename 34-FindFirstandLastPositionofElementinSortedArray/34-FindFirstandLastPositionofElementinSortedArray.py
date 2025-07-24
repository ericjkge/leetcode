# Last updated: 7/24/2025, 4:02:08 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def first(nums, target):
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            return -1
            
        def last(nums, target):
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
            if nums[right] == target:
                return right
            if nums[left] == target:
                return left
            return -1

        return [first(nums, target), last(nums, target)]