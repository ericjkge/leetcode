# Last updated: 10/23/2025, 10:34:01 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1 = p2 = 0
        ans = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
                while p1 < len(nums1) and nums1[p1] == nums1[p1 - 1]:
                    p1 += 1
                while p2 < len(nums2) and nums2[p2] == nums2[p2 - 1]:
                    p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return ans