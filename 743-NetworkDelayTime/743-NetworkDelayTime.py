# Last updated: 2/8/2026, 7:29:34 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        graph = defaultdict(list)
4
5        for u, v, w in times:
6            graph[u].append((v, w))
7        
8        distances = [float("inf")] * n
9        distances[k - 1] = 0
10        heap = [(0, k)]
11        time = 0
12
13        while heap:
14            dist, node = heapq.heappop(heap)
15            if dist > distances[node - 1]:
16                continue
17            
18            for neighbor, weight in graph[node]:
19                if distances[node - 1] + weight < distances[neighbor - 1]:
20                    distances[neighbor - 1] = distances[node - 1] + weight
21                    heapq.heappush(heap, (distances[neighbor - 1], neighbor))
22
23        ans = max(distances)        
24        return ans if ans != float("inf") else -1
25
26