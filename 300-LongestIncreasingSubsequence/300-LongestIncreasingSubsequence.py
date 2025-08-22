# Last updated: 8/22/2025, 6:36:25 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def dp(i):
            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dp(j))
            return best

        return max(dp(i) for i in range(n))