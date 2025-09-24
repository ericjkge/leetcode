# Last updated: 9/24/2025, 10:14:43 AM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = ans = 0
        window = 1

        while right < len(nums):
            window *= nums[right]
            while left <= right and window >= k:
                window //= nums[left]
                left += 1
            ans += (right - left + 1)
            right += 1

        return ans