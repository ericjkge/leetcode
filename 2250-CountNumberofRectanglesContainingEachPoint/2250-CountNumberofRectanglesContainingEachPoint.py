# Last updated: 7/19/2025, 2:12:37 PM
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def binarySearch(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = left + (right - left) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        hashmap = defaultdict(list)
        for l, h in rectangles:
            hashmap[h].append(l)
        
        for lengths in hashmap.values():
            lengths.sort()
        
        ans = []
        for x, y in points:
            count = 0
            for height in range(y, 101):
                lengths = hashmap[height]
                count += len(lengths) - binarySearch(lengths, x) 
            ans.append(count)
        
        return ans