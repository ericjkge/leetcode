# Last updated: 12/31/2025, 10:00:37 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        seen = set()
4        graph = defaultdict(list)
5
6        for u, v in edges:
7            graph[u].append(v)
8            graph[v].append(u)
9
10        def dfs(node, parent):
11            for neighbor in graph[node]:
12                if neighbor != parent and neighbor in seen:
13                    return False
14                if neighbor not in seen:
15                    seen.add(neighbor)
16                    if not dfs(neighbor, node):
17                        return False
18            return True
19            
20        seen.add(0)
21        if dfs(0, None) and len(seen) == n:
22            return True
23        return False
24        