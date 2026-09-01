# Last updated: 9/1/2026, 6:15:58 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
4        rows, cols = len(heights), len(heights[0])
5        pacific, atlantic = set(), set()
6
7        def dfs(r, c, s):
8            s.add((r, c))
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in s:
12                    dfs(nr, nc, s)
13
14        for r in range(rows):
15            dfs(r, 0, pacific)
16            dfs(r, cols - 1, atlantic)
17        
18        for c in range(cols):
19            dfs(0, c, pacific)
20            dfs(rows - 1, c, atlantic)
21
22        return list(pacific & atlantic)