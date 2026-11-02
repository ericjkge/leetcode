# Last updated: 11/2/2026, 4:28:42 PM
1class Solution:
2    def equalPairs(self, grid: list[list[int]]) -> int:
3        n = len(grid)
4        rows = defaultdict(int)
5        cols = defaultdict(int)
6
7        for r in range(n):
8            rows[tuple(grid[r])] += 1
9        
10        for c in range(n):
11            col = []
12            for r in range(n):
13                col.append(grid[r][c])
14            cols[tuple(col)] += 1
15        
16        count = 0
17        for key, val in rows.items():
18            count += val * cols[key]
19
20        return count