# Last updated: 5/30/2025, 12:07:21 PM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        length = len(bombs)
        graph = defaultdict(list)
        ans = 0
        
        for i in range(length):
            x, y, r = bombs[i]
            for j in range(length):
                x2, y2, _ = bombs[j]
                if r**2 >= (x-x2)**2 + (y-y2)**2:
                    graph[i].append(j)
        
        for i in range(length):
            seen = {i}
            dfs(i)
            ans = max(ans, len(seen))
        
        return ans
        