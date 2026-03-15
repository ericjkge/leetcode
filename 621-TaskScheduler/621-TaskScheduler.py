# Last updated: 3/15/2026, 11:24:15 AM
1class Solution:
2    def leastInterval(self, tasks: List[str], n: int) -> int:
3        cooldown = deque()
4        freqs = [-v for v in Counter(tasks).values()]
5        heapq.heapify(freqs)
6        time = 0
7
8        while freqs or cooldown:
9            while cooldown and cooldown[0][0] == time:
10                _, f = cooldown.popleft()
11                heapq.heappush(freqs, f)
12
13            if freqs:
14                freq = heapq.heappop(freqs)
15                freq += 1
16                if freq < 0:
17                    cooldown.append((time + n + 1, freq))
18            time += 1
19        
20        return time