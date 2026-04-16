# Last updated: 4/16/2026, 10:33:41 AM
1class Solution:
2    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
3        distances = [float("inf")] * n
4        distances[src] = 0
5        graph = defaultdict(list)
6
7        for a, b, price in flights:
8            graph[a].append((b, price))
9        
10        queue = deque([(0, src)])
11        counter = 0
12        while queue and counter <= k:
13            for _ in range(len(queue)):
14                dist, node = queue.popleft()
15                for neighbor, price in graph[node]:
16                    if dist + price < distances[neighbor]:
17                        distances[neighbor] = dist + price
18                        queue.append((dist + price, neighbor))
19            counter += 1
20        
21        return distances[dst] if distances[dst] != float("inf") else -1