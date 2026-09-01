# Last updated: 9/1/2026, 8:10:29 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = defaultdict(list)
4        indegrees = [0] * numCourses
5
6        for a, b in prerequisites:
7            graph[b].append(a)
8            indegrees[a] += 1
9
10        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
11        seen = len(queue)
12        while queue:
13            course = queue.popleft()
14            for neighbor in graph[course]:
15                indegrees[neighbor] -= 1
16                if indegrees[neighbor] == 0:
17                    seen += 1
18                    queue.append(neighbor)
19        
20        return seen == numCourses
21        