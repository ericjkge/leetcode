# Last updated: 8/12/2025, 2:41:44 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 # Left partition for A
            j = half - i - 2 # Left partition for B

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if i + 1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if j + 1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Bleft > Aright:
                left = i + 1
            else:
                right = i - 1
