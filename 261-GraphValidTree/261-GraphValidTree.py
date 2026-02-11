# Last updated: 2/11/2026, 2:34:19 PM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges) != n - 1:
4            return False
5
6        if not edges:
7            return True
8
9        graph = defaultdict(list)
10        for u, v in edges:
11            graph[u].append(v)
12            graph[v].append(u)
13
14        seen = set()
15        def dfs(node):
16            for neighbor in graph[node]:
17                if neighbor not in seen:
18                    seen.add(neighbor)
19                    dfs(neighbor)
20        
21        dfs(0)
22        return len(seen) == n