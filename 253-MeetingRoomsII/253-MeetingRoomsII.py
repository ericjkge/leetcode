# Last updated: 4/9/2026, 9:28:27 AM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        intervals.sort()
4        rooms = 0
5        ans = 0
6        heap = []
7
8        for start, end in intervals:
9            if not heap or start < heap[0]:
10                rooms += 1
11                heapq.heappush(heap, end)
12                ans = max(ans, rooms)
13            else:
14                heapq.heappop(heap)
15                heapq.heappush(heap, end)
16
17        return ans