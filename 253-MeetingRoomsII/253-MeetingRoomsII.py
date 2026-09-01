# Last updated: 9/1/2026, 10:09:19 AM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        intervals.sort()
4        heap = []
5        ans = 0
6
7        for start, end in intervals:
8            while heap and heap[0] <= start:
9                heapq.heappop(heap)
10            
11            heapq.heappush(heap, end)
12            ans = max(ans, len(heap))
13
14        return ans