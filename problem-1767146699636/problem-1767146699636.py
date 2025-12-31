# Last updated: 12/31/2025, 10:04:59 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        seen = set()
4        graph = defaultdict(list)
5
6        for u, v in edges:
7            graph[u].append(v)
8            graph[v].append(u)
9        
10        if len(edges) != n - 1:
11            return False
12        
13        def dfs(node):
14            for neighbor in graph[node]:
15                if neighbor not in seen:
16                    seen.add(neighbor)
17                    dfs(neighbor)
18        
19        seen.add(0)
20        dfs(0)
21        return len(seen) == n