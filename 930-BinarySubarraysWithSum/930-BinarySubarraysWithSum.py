# Last updated: 7/4/2025, 3:16:45 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(target):
            if target < 0:
                return 0
            left = total = ans = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > target:
                    total -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans
        return helper(goal) - helper(goal - 1)