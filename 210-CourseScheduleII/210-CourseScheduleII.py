# Last updated: 12/27/2025, 10:56:58 PM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4        indegrees = [0] * numCourses
5
6        for u, v in prerequisites:
7            graph[v].append(u)
8            indegrees[u] += 1
9        
10        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
11        order = []
12        counter = 0
13
14        while queue:
15            course = queue.popleft()
16            order.append(course)
17            counter += 1
18            for neighbor in graph[course]:
19                indegrees[neighbor] -= 1
20                if indegrees[neighbor] == 0:
21                    queue.append(neighbor)
22        
23        if counter != numCourses:
24            return []
25        return order