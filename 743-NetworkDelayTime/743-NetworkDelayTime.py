# Last updated: 4/8/2026, 5:35:53 PM
1class Solution:
2    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
3        distances = [float("inf")] * (n + 1)
4        distances[0] = 0    # 0-th index is unused
5        distances[k] = 0
6        graph = defaultdict(list)
7
8        for u, v, w in times:
9            graph[u].append((v, w))
10        
11        heap = [(0, k)]
12        while heap:
13            distance, node = heapq.heappop(heap)
14            if distance > distances[node]:
15                continue
16            for v, w in graph[node]:
17                if distance + w < distances[v]:
18                    distances[v] = distance + w
19                    heapq.heappush(heap, (distances[v], v))
20        
21        ans = max(distances)
22        return ans if ans != float("inf") else -1