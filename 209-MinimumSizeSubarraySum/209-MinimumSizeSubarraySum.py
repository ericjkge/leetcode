# Last updated: 9/24/2025, 10:02:47 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = right = 0
        window = 0

        while right < len(nums):
            window += nums[right]
            while window >= target:
                ans = min(ans, right - left + 1)
                window -= nums[left]
                left += 1
            right += 1

        return ans if ans != float("inf") else 0