# Last updated: 7/24/2025, 6:39:55 PM
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1
        
        while reader.get(right) < target:
            right *= 2
        
        while left + 1 < right:
            mid = (left + right) // 2
            if reader.get(mid) <= target:
                left = mid
            else:
                right = mid
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1