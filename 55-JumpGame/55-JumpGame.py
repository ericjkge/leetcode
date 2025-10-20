# Last updated: 10/20/2025, 2:00:25 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dp(i):
            if i >= n - 1:
                return True
            for j in range(1, nums[i] + 1):
                if dp(i + j):
                    return True
            return False

        return dp(0)