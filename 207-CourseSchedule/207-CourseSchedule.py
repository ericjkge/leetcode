# Last updated: 3/12/2026, 2:33:13 PM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        graph = defaultdict(list)
4        indegrees = defaultdict(int)
5
6        for a, b in prerequisites:
7            graph[b].append(a)
8            indegrees[a] += 1
9        
10        queue = deque([k for k in range(numCourses) if indegrees[k] == 0])
11        count = 0
12
13        while queue:
14            node = queue.popleft()
15            count += 1
16            for neighbor in graph[node]:
17                indegrees[neighbor] -= 1
18                if indegrees[neighbor] == 0:
19                    queue.append(neighbor)
20        
21        return count == numCourses