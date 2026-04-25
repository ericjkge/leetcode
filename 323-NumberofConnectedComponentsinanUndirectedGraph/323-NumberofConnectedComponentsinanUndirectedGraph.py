# Last updated: 4/25/2026, 1:04:22 PM
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
16        count = 0
17        for i in range(n):
18            if i not in seen:
19                dfs(i)
20                count += 1
21        
22        return count