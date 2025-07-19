# Last updated: 7/19/2025, 9:14:52 PM
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        startTimes = []
        endTimes = []
        for start, end in flowers:
            startTimes.append(start)
            endTimes.append(end + 1)

        startTimes.sort()
        endTimes.sort()

        ans = []

        def binarySearch(arr, target): # goes out by 1
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for person in people:
            ans.append(binarySearch(startTimes, person) - binarySearch(endTimes, person))

        return ans

        
        
