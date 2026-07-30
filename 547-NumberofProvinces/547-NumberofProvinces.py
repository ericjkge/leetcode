# Last updated: 7/29/2026, 9:17:32 PM
1class Solution:
2    def findCircleNum(self, isConnected: List[List[int]]) -> int:
3        n = len(isConnected)
4        graph = defaultdict(list)
5
6        for r in range(n):
7            for c in range(n):
8                if isConnected[r][c] == 1:
9                    graph[r].append(c)
10                    graph[c].append(r)
11        
12        def dfs(node):
13            seen.add(node)
14            for neighbor in graph[node]:
15                if neighbor not in seen:
16                    dfs(neighbor)
17
18        seen = set()
19        count = 0
20        for i in range(n):
21            if i not in seen:
22                dfs(i)
23                count += 1
24        
25        return count
26