# Last updated: 2/15/2026, 12:37:22 PM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        graph = defaultdict(list)
4
5        for a, b in edges:
6            graph[a].append(b)
7            graph[b].append(a)
8        
9        def dfs(node):
10            seen.add(node)
11            for neighbor in graph[node]:
12                if neighbor not in seen:
13                    dfs(neighbor)
14        
15        seen = set()
16        counter = 0
17
18        for node in range(n):
19            if node not in seen:
20                counter += 1
21                dfs(node)
22        
23        return counter