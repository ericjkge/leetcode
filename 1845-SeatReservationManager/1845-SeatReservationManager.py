# Last updated: 7/9/2025, 11:02:17 PM
class SeatManager:

    def __init__(self, n: int):
        self.marker = 1
        self.heap = []

    def reserve(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        
        seat = self.marker
        self.marker += 1
        return seat

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)