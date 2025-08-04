# Last updated: 8/4/2025, 6:41:48 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        seen = set()
        
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        for i in range(n): 
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
        
        return ans