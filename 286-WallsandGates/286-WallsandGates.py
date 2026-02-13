# Last updated: 2/13/2026, 9:33:53 AM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        INF = 2 ** 31 - 1
7        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
8        rows, cols = len(rooms), len(rooms[0])
9        gates = []
10
11        for r in range(rows):
12            for c in range(cols):
13                if rooms[r][c] == 0:
14                    gates.append((r, c))
15
16        queue = deque(gates)
17        distance = 1
18        seen = set(gates)
19
20        while queue:
21            for _ in range(len(queue)):
22                r, c = queue.popleft()
23                for dr, dc in directions:
24                    nr, nc = r + dr, c + dc
25                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and rooms[nr][nc] != -1:
26                        seen.add((nr, nc))
27                        queue.append((nr, nc))
28                        if rooms[nr][nc] == INF:
29                            rooms[nr][nc] = distance
30
31            distance += 1
32