# Last updated: 8/12/2026, 7:14:44 PM
1class Solution:
2    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
3        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
4        rows, cols = len(maze), len(maze[0])
5
6        queue = deque([entrance])
7        steps = 0
8        while queue:
9            for _ in range(len(queue)):
10                r, c = queue.popleft()
11                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and [r, c] != entrance:
12                    return steps
13                for dr, dc in directions:
14                    nr, nc = r + dr, c + dc
15                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
16                        maze[nr][nc] = "+"
17                        queue.append((nr, nc))
18            steps += 1
19        
20        return -1