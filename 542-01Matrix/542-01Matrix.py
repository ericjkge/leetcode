# Last updated: 8/8/2026, 4:37:29 PM
1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(mat), len(mat[0])
4        queue = deque()
5        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
6
7        for r in range(rows):
8            for c in range(cols):
9                if mat[r][c] == 0:
10                    queue.append((r, c))
11                else:
12                    mat[r][c] = "#"
13        
14        while queue:
15            r, c = queue.popleft()
16            for dr, dc in directions:
17                nr, nc = r + dr, c + dc
18                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == "#":
19                    mat[nr][nc] = mat[r][c] + 1
20                    queue.append((nr, nc))
21        
22        return mat