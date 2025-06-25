# Last updated: 6/25/2025, 2:41:35 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        return max_sum

