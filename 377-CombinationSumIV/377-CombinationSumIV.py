# Last updated: 9/5/2025, 10:03:48 AM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i):
            if i > target:
                return 0
            if i == target:
                return 1
            ways = 0
            for n in nums:
                ways += dp(i + n)
            return ways

        return dp(0)