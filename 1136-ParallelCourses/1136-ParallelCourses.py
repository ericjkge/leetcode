# Last updated: 8/21/2025, 7:54:58 PM
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        indegree = [0] * (n + 1)
        indegree[0] = -1 # Ignore 0th index (using 1-indexed indegree)
        
        for prev, nxt in relations:
            neighbors[prev].append(nxt)
            indegree[nxt] += 1
        
        # Add all 0 indegrees
        queue = deque([i for i in range(n + 1) if indegree[i] == 0])

        sems = 0
        counter = 0 
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                counter += 1
                for neighbor in neighbors[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            sems += 1
        
        return sems if counter == n else -1