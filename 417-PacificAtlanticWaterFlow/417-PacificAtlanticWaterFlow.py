# Last updated: 8/8/2026, 4:52:16 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(heights), len(heights[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        q1 = deque([(r, 0) for r in range(rows)] + [(0, c) for c in range(1, cols)])
6        q2 = deque([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows - 1)])
7        pacific, atlantic = set(), set()
8
9        while q1:
10            r, c = q1.popleft()
11            pacific.add((r, c))
12            for dr, dc in directions:
13                nr, nc = r + dr, c + dc
14                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pacific:
15                    q1.append((nr, nc))
16        
17        while q2:
18            r, c = q2.popleft()
19            atlantic.add((r, c))
20            for dr, dc in directions:
21                nr, nc = r + dr, c + dc
22                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atlantic:
23                    q2.append((nr, nc))
24
25        return list(pacific & atlantic)