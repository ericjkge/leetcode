# Last updated: 12/29/2025, 8:34:24 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        graph = defaultdict(list)
4
5        for u, v, w in times:
6            graph[u].append((v, w))
7        
8        distances = [float("inf")] * (n + 1) # Keep 0th index empty and use rest as 1-indexed
9        distances[0] = -1
10        distances[k] = 0
11        heap = [(0, k)]
12
13        while heap:
14            dist, node = heapq.heappop(heap)
15            if dist > distances[node]:
16                continue
17            
18            for neighbor, weight in graph[node]:
19                if dist + weight < distances[neighbor]:
20                    distances[neighbor] = dist + weight
21                    heapq.heappush(heap, (dist + weight, neighbor))
22        
23        return max(distances) if max(distances) != float("inf") else -1
24
25