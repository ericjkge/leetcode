# Last updated: 10/16/2025, 12:33:21 AM
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegrees = [0 for _ in range(n + 1)]
        indegrees[0] = -1
        queue = deque()

        for u, v in relations:
            graph[u].append(v)
            indegrees[v] += 1
        
        queue = deque([i for i in range(n + 1) if indegrees[i] == 0])
        ans = 0
        counter = 0 

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                counter += 1
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        queue.append(neighbor)
            ans += 1

        return ans if counter == n else -1