# Last updated: 4/15/2026, 8:46:27 PM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        rows, cols = len(rooms), len(rooms[0])
7        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
8        INF = 2147483647
9        queue = deque([])
10
11        for r in range(rows):
12            for c in range(cols):
13                if rooms[r][c] == 0:
14                    queue.append((r, c))
15        
16        counter = 1
17        while queue:
18            for _ in range(len(queue)):
19                r, c = queue.popleft()
20                for dr, dc in directions:
21                    nr, nc = r + dr, c + dc
22                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
23                        rooms[nr][nc] = counter
24                        queue.append((nr, nc))
25            counter += 1
26