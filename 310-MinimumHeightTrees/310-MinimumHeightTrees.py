# Last updated: 8/23/2025, 12:16:24 AM
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        degree = [0] * n

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            degree[start] += 1
            degree[end] += 1

        queue = deque([i for i in range(n) if degree[i] == 1])
        counter = n
        while counter > 2:
            counter -= len(queue)
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)
                        
        return [val for val in queue]