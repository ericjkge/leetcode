# Last updated: 7/2/2025, 12:54:58 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-f for f in freq.values()]
        heapq.heapify(max_heap)
        cooldown = deque() # ready time, count
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap) + 1
                if count != 0:
                    cooldown.append((time + n, count))
            
            if cooldown and cooldown[0][0] == time:
                time, count = cooldown.popleft()
                heapq.heappush(max_heap, count)
        
        return time
    