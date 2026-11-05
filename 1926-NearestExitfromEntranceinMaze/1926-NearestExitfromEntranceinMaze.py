# Last updated: 11/4/2026, 8:03:43 PM
1class Solution:
2    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
3        m, n = len(maze), len(maze[0])
4        queue = deque([tuple(entrance)])
5        maze[entrance[0]][entrance[1]] = "+"
6        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
7        steps = 0
8
9        while queue:
10            for _ in range(len(queue)):
11                r, c = queue.popleft()
12                for dr, dc in directions:
13                    nr, nc = r + dr, c + dc
14                    if not(0 <= nr < m and 0 <= nc < n) and steps != 0:
15                        return steps
16                    if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == ".":
17                        maze[nr][nc] = "+"
18                        queue.append((nr, nc))
19            steps += 1
20
21        return -1                
22