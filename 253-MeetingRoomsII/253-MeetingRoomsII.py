# Last updated: 2/9/2026, 5:12:03 PM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        intervals.sort()
4        heap = []
5        rooms = 0
6
7        for start, end in intervals:
8            while heap and start >= heap[0]:
9                heapq.heappop(heap)
10            heapq.heappush(heap, end)
11            # print(heap)
12            rooms = max(rooms, len(heap))
13
14        return rooms