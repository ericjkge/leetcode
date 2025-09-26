# Last updated: 9/26/2025, 9:32:25 AM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        seen = set()
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    dfs(neighbor)

        ans = 0
        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)
        return ans