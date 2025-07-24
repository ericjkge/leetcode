# Last updated: 7/25/2025, 12:05:37 AM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        
        def count(nums, target):
            counter = 0
            for n in nums:
                if n <= target:
                    counter += 1
            return counter
        
        while left + 1 < right:
            mid = (left + right) // 2
            if count(nums, mid) > mid:
                right = mid
            else:
                left = mid
        
        if count(nums, left) > left:
            return left
        return right
        