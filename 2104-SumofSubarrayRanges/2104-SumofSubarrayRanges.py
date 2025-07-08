# Last updated: 7/7/2025, 11:04:58 PM
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for left in range(len(nums)):
            min_val, max_val = float("inf"), -float("inf")
            for right in range(left, len(nums)):
                min_val = min(min_val, nums[right])
                max_val = max(max_val, nums[right])
                ans += (max_val - min_val)
        
        return ans