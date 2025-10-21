# Last updated: 10/21/2025, 3:14:05 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        intervals.sort()
        max_rooms = 1

        for start, end in intervals:
            if not events:
                heapq.heappush(events, (end, max_rooms))
            else:
                if events[0][0] > start:
                    max_rooms += 1
                    heapq.heappush(events, (end, max_rooms)) 
                else:
                    _, room_number = heapq.heappop(events)
                    heapq.heappush(events, (end, room_number))

        return max_rooms