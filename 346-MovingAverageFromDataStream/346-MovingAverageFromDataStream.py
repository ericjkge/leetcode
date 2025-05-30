# Last updated: 5/30/2025, 12:07:54 PM
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.count = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        
        self.count += 1
        self.queue.append(val)
        
        tail = self.queue.popleft() if self.count > self. size else 0

        self.window_sum = self.window_sum + val - tail
            
        return self.window_sum/min(self.count, self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)

# param_1 = obj.next(val)