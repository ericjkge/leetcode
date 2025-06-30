# Last updated: 6/30/2025, 1:21:00 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        print(in_degree)
        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1
        
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        taken = 0

        while queue:
            pre = queue.popleft()
            taken += 1
            for crs in graph[pre]:
                in_degree[crs] -= 1
                if in_degree[crs] == 0:
                    queue.append(crs)
        
        return taken == numCourses
        
        print(graph)
        print(in_degree)