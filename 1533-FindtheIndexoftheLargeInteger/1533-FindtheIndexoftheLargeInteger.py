# Last updated: 7/19/2025, 2:59:29 PM
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            size = right - left + 1
            mid = left + (right - left) // 2
            if size % 2 == 0:
                if reader.compareSub(left, mid, mid + 1, right) == -1:
                    left = mid + 1
                else:
                    right = mid
            else:
                result = reader.compareSub(left, mid - 1, mid + 1, right)
                if result == 0:
                    return mid
                if result == -1:
                    left = mid + 1
                else:
                    right = mid - 1
        return left