# Last updated: 1/2/2026, 10:50:04 AM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        graph = defaultdict(list)
4        for start, end, cost in flights:
5            graph[start].append((end, cost))
6        
7        distances = [float("inf")] * n
8        distances[src] = 0
9
10        queue = deque([(src, 0)])
11        stops = 0
12        while queue:
13            for _ in range(len(queue)):
14                node, dist = queue.popleft()
15
16                for neighbor, weight in graph[node]:
17                    if dist + weight < distances[neighbor]:
18                        distances[neighbor] = dist + weight
19                        queue.append((neighbor, dist + weight))
20
21            stops += 1
22            if stops > k:
23                break
24
25        return distances[dst] if distances[dst] != float("inf") else -1