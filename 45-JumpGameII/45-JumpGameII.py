# Last updated: 11/17/2025, 10:04:04 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i > n - 1:
                return float("inf")

            if i == n - 1:
                return 0
            
            best = float("inf")

            for j in range(1, nums[i] + 1):
                best = min(best, 1 + dp(i + j))

            return best
                
        return dp(0)