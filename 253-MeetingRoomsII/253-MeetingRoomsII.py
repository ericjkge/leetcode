# Last updated: 10/21/2025, 3:15:33 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        intervals.sort()
        max_rooms = 1

        for start, end in intervals:
            if not events:
                heapq.heappush(events, (end))
            else:
                if events[0] > start:
                    max_rooms += 1
                else:
                    heapq.heappop(events)
                heapq.heappush(events, (end))

        return max_rooms