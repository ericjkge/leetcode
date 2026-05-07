# Last updated: 5/7/2026, 1:18:09 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(heights), len(heights[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5
6        def dfs(r, c, s):
7            s.add((r, c))
8            for dr, dc in directions:
9                nr, nc = r + dr, c + dc
10                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in s:
11                    dfs(nr, nc, s)
12        
13        pacific = set()
14        for r in range(rows):
15            dfs(r, 0, pacific)
16        
17        for c in range(cols):
18            dfs(0, c, pacific)
19        
20        atlantic = set()
21        for r in range(rows):
22            dfs(r, cols - 1, atlantic)
23        
24        for c in range(cols):
25            dfs(rows - 1, c, atlantic)
26        
27        return [[r, c] for r, c in pacific & atlantic]