# Last updated: 6/14/2026, 10:57:08 AM
1class Solution:
2    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(mat), len(mat[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        queue = deque()
6
7        for r in range(rows):
8            for c in range(cols):
9                if mat[r][c] == 0:
10                    queue.append((r, c))
11                else:
12                    mat[r][c] = -1
13        
14        while queue:
15            r, c = queue.popleft()
16            for dr, dc in directions:
17                nr, nc = r + dr, c + dc
18                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
19                    mat[nr][nc] = mat[r][c] + 1
20                    queue.append((nr, nc))
21        
22        return mat
23            