# Last updated: 7/19/2025, 9:20:45 PM
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        
        starts.sort()
        ends.sort()
        ans = []

        def binarySearch(arr, target): # Goes over by 1
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        for person in people:
            ans.append(binarySearch(starts, person) - binarySearch(ends, person))
        
        return ans