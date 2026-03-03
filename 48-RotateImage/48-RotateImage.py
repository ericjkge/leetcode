# Last updated: 3/3/2026, 8:49:14 AM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        rows, cols = len(matrix), len(matrix[0])
7
8        for r in range(rows):
9            for c in range(cols):
10                if r < c:
11                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
12
13        for row in matrix:
14            row.reverse()
15        
16        return matrix
17
18                    # 147
19                    # 258
20                    # 369