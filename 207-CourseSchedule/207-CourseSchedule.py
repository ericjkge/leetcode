# Last updated: 12/27/2025, 10:33:35 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = defaultdict(list)
4        indegrees = [0] * numCourses
5
6        for u, v in prerequisites:
7            graph[v].append(u)
8            indegrees[u] += 1
9        
10        counter = 0
11        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
12
13        while queue:
14            course = queue.popleft()
15            counter += 1
16            for neighbor in graph[course]:
17                indegrees[neighbor] -= 1
18                if indegrees[neighbor] == 0:
19                    queue.append(neighbor)
20
21        return counter == numCourses