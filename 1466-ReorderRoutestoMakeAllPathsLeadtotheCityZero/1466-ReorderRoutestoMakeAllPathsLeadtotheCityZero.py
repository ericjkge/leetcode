# Last updated: 7/29/2026, 9:49:46 PM
1class Solution:
2    def minReorder(self, n: int, connections: List[List[int]]) -> int:
3        original = set((u, v) for u, v in connections)
4        graph = defaultdict(list)
5
6        for u, v in connections:
7            graph[u].append(v)
8            graph[v].append(u)
9        
10        seen = set()
11        self.count = 0
12        def dfs(node):
13            seen.add(node)
14            for neighbor in graph[node]:
15                if neighbor not in seen:
16                    if (neighbor, node) not in original:
17                        self.count += 1
18                    dfs(neighbor)
19        
20        dfs(0)
21        return self.count
22