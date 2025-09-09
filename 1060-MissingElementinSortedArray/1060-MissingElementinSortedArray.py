# Last updated: 9/9/2025, 3:32:16 PM
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def findMissing(i):
            return nums[i] - nums[0] - i

        left, right = 0, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if findMissing(mid) >= k:
                right = mid
            else:
                left = mid

        return nums[left] + (k - findMissing(left))