# Last updated: 9/6/2025, 2:32:23 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort()
        rooms, max_rooms = 0, 0

        for time, delta in events:
            rooms += delta
            max_rooms = max(max_rooms, rooms)
        
        return max_rooms