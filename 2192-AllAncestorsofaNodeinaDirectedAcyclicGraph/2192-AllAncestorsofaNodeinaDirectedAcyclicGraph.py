# Last updated: 7/9/2025, 4:46:05 PM
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = []
        graph = defaultdict(list)
        for a, b in edges:
            graph[b].append(a)
        
        def dfs(node, ancestors):
            for child in graph[node]:
                if child not in ancestors:
                    ancestors.add(child)
                    dfs(child, ancestors)

        for i in range(n):
            ancestors = set()
            dfs(i, ancestors)
            ans.append(sorted(ancestors))

        return ans