# Last updated: 1/29/2026, 10:24:46 AM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        cooldown = deque()
4        freqs = Counter(tasks)
5        heap = [(-val, key) for key, val in freqs.items()]
6        heapq.heapify(heap)
7        time = 0
8
9        while heap or cooldown:
10            if heap:
11                freq, task = heapq.heappop(heap)
12                freq *= -1
13                freq -= 1
14                
15                if freq != 0:
16                    cooldown.append((time + n, task, freq))
17
18            if cooldown and cooldown[0][0] == time:
19                _, t, f = cooldown.popleft()
20                heapq.heappush(heap, (-f, t))
21            
22            time += 1
23
24        return time