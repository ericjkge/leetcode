# Last updated: 6/10/2026, 10:27:11 PM
1class Solution:
2    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
3        graph = defaultdict(list)
4
5        for u, v in edges:
6            graph[u].append(v)
7            graph[v].append(u)
8
9        seen = {1}
10        queue = deque([1])
11        counter = -1
12        while queue:
13            for _ in range(len(queue)):
14                node = queue.popleft()
15                for neighbor in graph[node]:
16                    if neighbor not in seen:
17                        seen.add(neighbor)
18                        queue.append(neighbor)
19            counter += 1
20        
21        return pow(2, counter - 1, 10**9 + 7)
22