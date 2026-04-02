# Last updated: 4/2/2026, 9:51:38 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = defaultdict(list)
4        indegrees = [0] * numCourses
5
6        for u, v in prerequisites:
7            graph[v].append(u)
8            indegrees[u] += 1
9    
10        count = 0
11        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
12        while queue:
13            count += 1
14            node = queue.popleft()
15            for neighbor in graph[node]:
16                indegrees[neighbor] -= 1
17                if indegrees[neighbor] == 0:
18                    queue.append(neighbor)
19        
20        return count == numCourses