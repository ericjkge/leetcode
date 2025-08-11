# Last updated: 8/11/2025, 3:54:26 PM
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Condition 1: E = V - 1
        if len(edges) != n - 1:
            return False
        
        # Condition 2: Connected (any two conditions imply the third)
        seen = set()
        def dfs(node):
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
        
        dfs(0)
        return True if len(seen) == n else False