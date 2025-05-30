# Last updated: 5/30/2025, 12:07:28 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            minimum = min(minimum, curr)
        return abs(minimum) + 1
        