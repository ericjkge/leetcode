# Last updated: 5/30/2025, 12:07:18 PM
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.ans = 1
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    self.ans += 1
                    seen.add(neighbor)
                    dfs(neighbor)
        
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
    
        seen = {0}
        for node in restricted:
            seen.add(node)
        
        dfs(0)
        return self.ans