# Last updated: 6/28/2025, 12:42:48 AM
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        edge_count = {}
        leaves = deque()
        for source, neighbors in graph.items():
            if len(neighbors) == 1:
                leaves.append(source)
            edge_count[source] = len(neighbors)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neighbor in graph[leaf]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)