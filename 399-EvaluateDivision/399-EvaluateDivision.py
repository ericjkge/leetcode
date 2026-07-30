# Last updated: 7/29/2026, 10:56:05 PM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        graph = defaultdict(list)
4        for (u, v), w in zip(equations, values):
5            graph[u].append((v, w))
6            graph[v].append((u, 1/w))
7        
8        def dfs(node, target, cost, seen):
9            if node == target:
10                return cost
11            seen.add(node)
12            for neighbor, weight in graph[node]:
13                if neighbor not in seen:
14                    res = dfs(neighbor, target, cost * weight, seen)
15                    if res is not None:
16                        return res
17            return None
18
19        ans = []
20        for a, b in queries:
21            if a not in graph or b not in graph:
22                ans.append(-1)
23            else:
24                res = dfs(a, b, 1, set())
25                ans.append(res if res is not None else -1)
26        return ans