# Last updated: 1/6/2026, 10:02:39 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph = defaultdict(list)
4        
5        for u, v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8
9        def dfs(node):
10            for neighbor in graph[node]:
11                if neighbor not in seen:
12                    seen.add(neighbor)
13                    dfs(neighbor)
14        
15        seen = set()
16        counter = 0
17
18        for i in range(n):
19            if i not in seen:
20                seen.add(i)
21                dfs(i)
22                counter += 1
23        
24        return counter