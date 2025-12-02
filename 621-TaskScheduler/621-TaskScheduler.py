# Last updated: 12/2/2025, 10:22:50 AM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        freqs = Counter(tasks)
4        max_heap = [-f for f in freqs.values()]
5        heapq.heapify(max_heap)
6        cooldown = deque()
7        time = 0
8
9        while max_heap or cooldown:
10            time += 1
11
12            if max_heap:
13                freq = heapq.heappop(max_heap) + 1
14                if freq < 0:
15                    cooldown.append((time + n, freq))
16            
17            if cooldown and cooldown[0][0] == time:
18                heapq.heappush(max_heap, cooldown.popleft()[1])
19        
20        return time
21
22