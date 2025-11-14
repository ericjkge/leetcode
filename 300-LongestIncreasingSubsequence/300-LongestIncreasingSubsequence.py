# Last updated: 11/14/2025, 10:42:01 AM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            best = 1

            for j in range(0, i):
                if nums[j] < nums[i]:
                    best = max(best, 1 + dp(j))
            
            return best

        return max(dp(i) for i in range(n))