# Last updated: 12/30/2025, 11:58:48 PM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        rooms = 0
4        waiting = []
5        intervals.sort()
6
7        for start, end in intervals:
8            while waiting and waiting[0] <= start:
9                heapq.heappop(waiting)
10
11            if not waiting or start < waiting[0]:
12                heapq.heappush(waiting, end)
13                rooms = max(rooms, len(waiting))
14        
15        return rooms