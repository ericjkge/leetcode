# Last updated: 9/3/2025, 10:37:52 AM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(total):
            if total > target:
                return 0

            if total == target:
                return 1
            
            ways = 0
            for num in nums:
                ways += dp(total + num)
            return ways

        return dp(0)
