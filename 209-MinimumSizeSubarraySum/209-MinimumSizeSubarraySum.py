# Last updated: 7/3/2025, 10:49:25 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        left = total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1
        
        return min_length if min_length != float("inf") else 0