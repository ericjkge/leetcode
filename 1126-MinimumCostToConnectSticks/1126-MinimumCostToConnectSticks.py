# Last updated: 5/30/2025, 12:07:37 PM
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        stick_list = [stick for stick in sticks]
        heapq.heapify(stick_list)
        while len(stick_list) > 1:
            stick1 = heapq.heappop(stick_list)
            stick2 = heapq.heappop(stick_list)
            heapq.heappush(stick_list, stick1 + stick2)
            cost += (stick1 + stick2)
        
        return cost
        