# Last updated: 9/6/2025, 2:32:45 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))

        events.sort()
        rooms, min_rooms = 0, 0

        for time, delta in events:
            rooms += delta
            min_rooms = max(min_rooms, rooms)
        
        return min_rooms