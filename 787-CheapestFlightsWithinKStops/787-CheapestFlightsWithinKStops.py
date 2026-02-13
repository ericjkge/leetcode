# Last updated: 2/13/2026, 11:50:52 AM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        graph = defaultdict(list)
4
5        for u, v, p in flights:
6            graph[u].append((v, p))
7
8        distances = [float("inf")] * n
9        distances[src] = 0
10        queue = deque([(0, src)])
11        stops = 0
12
13        while stops < k + 1:
14            for _ in range(len(queue)):
15                dist, node = queue.popleft()
16                
17                for neighbor, weight in graph[node]:
18                    d = dist + weight
19                    if d < distances[neighbor]:
20                        distances[neighbor] = d
21                        queue.append((d, neighbor))
22            stops += 1
23            
24        return distances[dst] if distances[dst] != float("inf") else -1