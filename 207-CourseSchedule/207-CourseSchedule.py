# Last updated: 6/30/2025, 1:24:54 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degrees[crs] += 1
        
        queue = deque(i for i in range(numCourses) if in_degrees[i] == 0)
        taken = 0

        while queue:
            pre = queue.popleft()
            taken += 1
            for crs in graph[pre]:
                in_degrees[crs] -= 1
                if in_degrees[crs] == 0:
                    queue.append(crs)
        
        return taken == numCourses
