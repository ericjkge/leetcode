# Last updated: 7/29/2026, 10:53:16 PM
1class Solution:
2    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
3        ans = []
4        graph = defaultdict(list)
5        chars = set()
6
7        for (u, v), w in zip(equations, values):
8            chars.add(u)
9            chars.add(v)
10            graph[u].append((v, w))
11            graph[v].append((u, 1/w))
12        
13        def dfs(node, target, cost):
14            if node == target:
15                return cost
16            
17            seen.add(node)
18            
19            ans = None
20            for neighbor, weight in graph[node]:
21                if neighbor not in seen:
22                    res = dfs(neighbor, target, cost * weight)
23                    if res != float("-inf"):
24                        return res
25            
26            return float("-inf")
27
28        for a, b in queries:
29            seen = set()
30            if a not in chars or b not in chars:
31                ans.append(-1)
32                continue
33            res = dfs(a, b, 1)
34            if res == float("-inf"):
35                ans.append(-1)
36                continue
37            ans.append(res)
38
39        return ans