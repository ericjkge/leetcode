# Last updated: 2/6/2026, 9:57:31 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = defaultdict(list)
4        indegree = [0] * numCourses
5
6        for u, v in prerequisites:
7            graph[v].append(u)
8            indegree[u] += 1
9        
10        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
11        counter = 0
12        while queue:
13            course = queue.popleft()
14            counter += 1
15            for neighbor in graph[course]:
16                indegree[neighbor] -= 1
17                if indegree[neighbor] == 0:
18                    queue.append(neighbor)
19        
20        return counter == numCourses
21
22