# Last updated: 2/13/2026, 9:35:10 AM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        INF = 2 ** 31 - 1
7        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
8        rows, cols = len(rooms), len(rooms[0])
9        queue = deque()
10
11        for r in range(rows):
12            for c in range(cols):
13                if rooms[r][c] == 0:
14                    queue.append((r, c))
15
16        distance = 1
17
18        while queue:
19            for _ in range(len(queue)):
20                r, c = queue.popleft()
21                for dr, dc in directions:
22                    nr, nc = r + dr, c + dc
23                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
24                        queue.append((nr, nc))
25                        rooms[nr][nc] = distance
26
27            distance += 1
28