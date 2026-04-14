# Last updated: 4/14/2026, 9:38:45 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges) != n - 1:
4            return False
5        
6        graph = defaultdict(list)
7        for a, b in edges:
8            graph[a].append(b)
9            graph[b].append(a)
10
11        seen = set()
12        def dfs(node):
13            seen.add(node)
14            for neighbor in graph[node]:
15                if neighbor not in seen:
16                    dfs(neighbor)
17        
18        dfs(0)
19        return len(seen) == n
20