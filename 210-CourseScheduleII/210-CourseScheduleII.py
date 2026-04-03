# Last updated: 4/3/2026, 9:13:57 AM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4        indegrees = [0] * numCourses
5
6        for a, b in prerequisites:
7            graph[b].append(a)
8            indegrees[a] += 1
9        
10        order = []
11        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
12        while queue:
13            course = queue.popleft()
14            order.append(course)
15            for neighbor in graph[course]:
16                indegrees[neighbor] -= 1
17                if indegrees[neighbor] == 0:
18                    queue.append(neighbor)
19        
20        return order if len(order) == numCourses else []