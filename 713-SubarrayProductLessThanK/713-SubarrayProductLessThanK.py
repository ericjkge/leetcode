# Last updated: 10/21/2025, 2:56:12 PM
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = right = ans = 0
        window = 1

        while right < len(nums):
            window *= nums[right]
            while left < right and window >= k:
                window /= nums[left]
                left += 1
            if window < k:
                ans += (right - left + 1)
            right += 1


        return ans