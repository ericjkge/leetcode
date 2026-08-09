# Last updated: 8/9/2026, 12:05:15 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        indegrees = [0] * numCourses
4        graph = defaultdict(list)
5
6        for a, b in prerequisites:
7            graph[b].append(a)
8            indegrees[a] += 1
9        
10        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
11        seen = set()
12        while queue:
13            node = queue.popleft()
14            seen.add(node)
15            for neighbor in graph[node]:
16                indegrees[neighbor] -= 1
17                if indegrees[neighbor] == 0:
18                    queue.append(neighbor)
19        
20        return len(seen) == numCourses
21