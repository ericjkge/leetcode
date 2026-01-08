# Last updated: 1/8/2026, 10:32:55 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(heights), len(heights[0])
4        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
5        pacific = set()
6        atlantic = set()
7
8        def dfs(r, c, s):
9            s.add((r, c))
10            for dr, dc in directions:
11                nr, nc = r + dr, c + dc
12                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in s and heights[r][c] <= heights[nr][nc]:
13                    dfs(nr, nc, s)
14        
15        for c in range(cols):
16            dfs(0, c, pacific)
17        
18        for r in range(rows):
19            dfs(r, 0, pacific)
20        
21        for c in range(cols):
22            dfs(rows - 1, c, atlantic)
23        
24        for r in range(rows):
25            dfs(r, cols - 1, atlantic)
26
27        ans = []
28
29        for r in range(rows):
30            for c in range(cols):
31                if (r, c) in atlantic and (r, c) in pacific:
32                    ans.append([r, c])
33        
34        return ans