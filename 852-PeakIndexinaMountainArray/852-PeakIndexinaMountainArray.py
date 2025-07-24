# Last updated: 7/24/2025, 10:26:17 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)
        
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid
        
        if arr[left] < arr[right]:
            return right
        return left