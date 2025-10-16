# Last updated: 10/16/2025, 10:53:48 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            if i >= n - 1:
                return 0
            res = float("inf")
            for j in range(1, nums[i] + 1):
                res = min(res, 1 + dp(i + j))
            return res

        return dp(0)