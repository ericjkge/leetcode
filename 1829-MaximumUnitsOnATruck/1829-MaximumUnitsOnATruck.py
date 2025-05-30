# Last updated: 5/30/2025, 12:07:25 PM
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [(-boxTypes[i][1], boxTypes[i][0]) for i in range(len(boxTypes))] # size, no. of boxes
        heapq.heapify(heap)
        
        ans = 0
        while truckSize > 0 and heap:
            curr = heapq.heappop(heap)
            if truckSize >= curr[1]:
                truckSize -= curr[1]
                ans += -curr[0] * curr[1]
            else:
                ans += (-curr[0] * truckSize)
                break
        
        return ans