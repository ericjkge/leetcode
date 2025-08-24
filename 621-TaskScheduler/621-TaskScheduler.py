# Last updated: 8/24/2025, 11:47:18 AM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0
        print(max_heap)
        while max_heap or cooldown:
            time += 1

            if max_heap:
                freq = heapq.heappop(max_heap)
                freq += 1
                if freq != 0:
                    cooldown.append((time + n, freq))
            
            if cooldown:
                if cooldown[0][0] == time:
                    _, freq = cooldown.popleft()
                    heapq.heappush(max_heap, freq)

        return time











        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    cooldown.append((time + n, count))
            
            if cooldown and cooldown[0][0] == time:
                heapq.heappush(max_heap, cooldown.popleft()[1])
        
        return time