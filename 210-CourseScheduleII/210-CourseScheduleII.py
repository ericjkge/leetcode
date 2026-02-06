# Last updated: 2/6/2026, 10:15:16 AM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        graph = defaultdict(list)
4        indegree = [0] * numCourses
5
6        for a, b in prerequisites:
7            graph[b].append(a)
8            indegree[a] += 1
9
10        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
11        order = []
12
13        while queue:
14            node = queue.popleft()
15            order.append(node)
16            for neighbor in graph[node]:
17                indegree[neighbor] -= 1
18                if indegree[neighbor] == 0:
19                    queue.append(neighbor)
20        
21        return order if len(order) == numCourses else []