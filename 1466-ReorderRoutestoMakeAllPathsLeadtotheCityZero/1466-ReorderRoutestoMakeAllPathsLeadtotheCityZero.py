# Last updated: 7/29/2026, 10:02:15 PM
1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        graph = defaultdict(list)
4
5        for u, v in connections:
6            graph[u].append((v, 1))
7            graph[v].append((u, 0))
8        
9        seen = set()
10        self.cost = 0
11        def dfs(node):
12            seen.add(node)
13            for neighbor, weight in graph[node]:
14                if neighbor not in seen:
15                    self.cost += weight
16                    dfs(neighbor)
17        
18        dfs(0)
19        return self.cost
20