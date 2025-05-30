# Last updated: 5/30/2025, 12:07:56 PM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        ans = 0
        
        seen = set()
        
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        
        return ans