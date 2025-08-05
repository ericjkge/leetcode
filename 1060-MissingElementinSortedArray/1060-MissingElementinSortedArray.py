# Last updated: 8/5/2025, 10:20:59 PM
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing(index):
            return nums[index] - nums[0] - index
        
        left, right = 0, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if missing(mid) < k:
                left = mid
            else:
                right = mid
        
        return nums[left] + k - missing(left)