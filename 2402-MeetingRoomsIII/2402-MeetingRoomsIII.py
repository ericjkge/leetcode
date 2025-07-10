# Last updated: 7/10/2025, 5:05:50 PM
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counter = [0] * n
        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)
        used_rooms = []

        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                heapq.heappush(free_rooms, heapq.heappop(used_rooms)[1])
            if free_rooms:
                room = heapq.heappop(free_rooms)
                counter[room] += 1
                heapq.heappush(used_rooms, (end, room))
            else:
                duration = end - start
                start = used_rooms[0][0]
                end = start + duration
                room = heapq.heappop(used_rooms)[1]
                counter[room] += 1
                heapq.heappush(used_rooms, (end, room))
        
        max_counter = max(counter)
        for i in range(len(counter)):
            if counter[i] == max_counter:
                return i

