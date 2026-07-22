# Last updated: 7/21/2026, 7:34:39 PM
1class Solution:
2    def equalPairs(self, grid: List[List[int]]) -> int:
3        n = len(grid)
4        seen = defaultdict(int)
5        count = 0
6
7        for row in grid:
8            seen[tuple(row)] += 1
9
10        for c in range(n):
11            col = []
12            for r in range(n):
13                col.append(grid[r][c])
14            
15            count += seen[tuple(col)]
16    
17        return count