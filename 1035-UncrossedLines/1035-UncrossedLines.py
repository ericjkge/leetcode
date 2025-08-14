# Last updated: 8/15/2025, 12:41:25 AM
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        a, b = len(nums1), len(nums2)

        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0

            if nums1[i] == nums2[j]:
                return 1 + dp(i - 1, j - 1)
            
            return max(dp(i - 1, j), dp(i, j - 1))

        return dp(a - 1, b - 1)