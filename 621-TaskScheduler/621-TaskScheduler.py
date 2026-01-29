# Last updated: 1/29/2026, 10:26:57 AM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        cooldown = deque()
4        freqs = Counter(tasks)
5        heap = [-f for f in freqs.values()]
6        heapq.heapify(heap)
7        time = 0
8
9        while heap or cooldown:
10            if heap:
11                freq = heapq.heappop(heap)
12                freq += 1
13                
14                if freq != 0:
15                    cooldown.append((time + n, freq))
16
17            if cooldown and cooldown[0][0] == time:
18                heapq.heappush(heap, cooldown.popleft()[1])
19            
20            time += 1
21
22        return time