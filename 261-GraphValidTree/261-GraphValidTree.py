# Last updated: 6/7/2026, 11:03:47 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        seen = set()
4        graph = defaultdict(list)
5
6        for a, b in edges:
7            graph[a].append(b)
8            graph[b].append(a)
9
10        def dfs(node):
11            seen.add(node)
12            for neighbor in graph[node]:
13                if neighbor not in seen:
14                    dfs(neighbor)
15
16        dfs(0)
17        return len(edges) == n - 1 and len(seen) == n