# Last updated: 6/29/2026, 8:34:37 PM
1class Solution:
2    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
3        m, n = len(matrix), len(matrix[0])
4        starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
5
6        for r, c in starts:
7            i, j = r, c
8            start = matrix[i][j]
9            while i < m and j < n:
10                if matrix[i][j] != start:
11                    return False
12                i += 1
13                j += 1
14        
15        return True