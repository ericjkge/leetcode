# Last updated: 7/18/2025, 10:31:47 PM
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for i in range(len(nums1)):
            left, right = i, len(nums2)
            while left < right:
                mid = left + (right - left) // 2
                if nums1[i] <= nums2[mid]:
                    left = mid + 1
                else:
                    right = mid
            ans = max(ans, left - i - 1)
        
        return ans