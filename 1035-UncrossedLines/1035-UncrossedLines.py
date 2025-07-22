# Last updated: 7/22/2025, 3:27:29 PM
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, j):
            if i < 0 or j < 0:
                return 0
            
            if nums1[i] == nums2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))
            
        return dp(len(nums1) - 1, len(nums2) - 1)