# Last updated: 8/16/2025, 11:35:03 AM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i):
            if i == 0:
                return 1
            
            if i < 0:
                return 0

            res = 0
            for num in nums:
                res += dp(i - num)
            return res

        return dp(target)