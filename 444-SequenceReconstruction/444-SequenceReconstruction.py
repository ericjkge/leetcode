# Last updated: 9/1/2026, 9:18:43 AM
1class Solution:
2    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
3        n = len(nums)
4        graph = defaultdict(list)
5        indegrees = [0] * (n + 1)
6
7        for sequence in sequences:
8            for i in range(len(sequence) - 1):
9                u, v = sequence[i], sequence[i + 1]
10                graph[u].append(v)
11                indegrees[v] += 1
12        
13        index = 0
14        queue = deque([i for i in range(1, n + 1) if indegrees[i] == 0])
15        while queue:
16            if len(queue) > 1:
17                return False
18            node = queue.popleft()
19            if node != nums[index]:
20                return False
21            for neighbor in graph[node]:
22                indegrees[neighbor] -= 1
23                if indegrees[neighbor] == 0:
24                    queue.append(neighbor)
25            index += 1
26
27        return index == n