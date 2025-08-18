# Last updated: 8/18/2025, 9:57:24 PM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i):
            if i == target:
                return 1
            if i > target:
                return 0
            ways = 0
            for num in nums:
                ways += dp(i + num)
            return ways
            
        return dp(0)