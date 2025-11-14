# Last updated: 11/14/2025, 2:09:56 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals.sort()
        ans = 0

        for start, end in intervals:
            while heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            ans = max(ans, len(heap))
        
        return ans