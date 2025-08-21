# Last updated: 8/21/2025, 7:50:20 PM
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        queue = deque()
        neighbors = defaultdict(list)
        indegree = [0] * n
        
        for prev, nxt in relations:
            neighbors[prev].append(nxt)
            indegree[nxt - 1] += 1 # Switch to 0 indexed
        
        # Add all 0 indegrees
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i + 1)
        
        sems = 0
        counter =0 
        while queue:
            for _ in range(len(queue)):
                course = queue.popleft()
                counter += 1
                for neighbor in neighbors[course]:
                    indegree[neighbor - 1] -= 1
                    if indegree[neighbor - 1] == 0:
                        queue.append(neighbor)
            sems += 1
        
        return sems if counter == n else -1