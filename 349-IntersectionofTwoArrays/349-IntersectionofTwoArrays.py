# Last updated: 7/26/2025, 11:53:48 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        p1 = p2 = 0
        
        nums1.sort()
        nums2.sort()
        
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                if not ans or nums1[p1] != ans[-1]:
                    ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
                
        return ans