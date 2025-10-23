# Last updated: 10/23/2025, 10:26:20 AM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
        # p1 = p2 = 0
        # l1, l2 = len(nums1), len(nums2)
        # ans = set()

        # while p1 < l1 and p2 < l2:
            

        # return ans