# Last updated: 2/18/2026, 1:48:56 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        result = []
4        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
5        rows, cols = len(heights), len(heights[0])
6
7        def dfs(r, c, s):
8            s.add((r, c))
9            for dr, dc in directions:
10                nr, nc = r + dr, c + dc
11                if 0 <= nr < rows and 0 <= nc < cols and heights[r][c] <= heights[nr][nc] and (nr, nc) not in s:
12                    dfs(nr, nc, s) 
13        
14        pacific = set()
15        atlantic = set()
16
17        for c in range(cols):
18            dfs(0, c, pacific)
19        
20        for r in range(rows):
21            dfs(r, 0, pacific)
22        
23        for c in range(cols):
24            dfs(rows - 1, c, atlantic)
25        
26        for r in range(rows):
27            dfs(r, cols - 1, atlantic)
28
29        both = pacific & atlantic
30        return [[r, c] for r, c in both]