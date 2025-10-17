# Last updated: 10/17/2025, 11:55:39 AM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            best = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    best = max(best, 1 + dp(j))
            return best
        
        return max(dp(i) for i in range(n))