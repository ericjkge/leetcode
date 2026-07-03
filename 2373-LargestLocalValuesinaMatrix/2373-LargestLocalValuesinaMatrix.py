# Last updated: 7/2/2026, 10:39:42 PM
1class Solution:
2    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
3        n = len(grid)
4        res = [[0] * (n - 2) for _ in range(n - 2)]
5
6        for i in range(n - 2):
7            for j in range(n - 2):
8                mx = 0
9                for r in range(i, i + 3):
10                    for c in range(j, j + 3):
11                        mx = max(mx, grid[r][c])
12                res[i][j] = mx
13
14        return res
15