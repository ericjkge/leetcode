# Last updated: 6/27/2026, 12:05:45 PM
1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        n = len(matrix)
7
8        for r in range(n):
9            for c in range(r, n):
10                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
11        
12        for row in matrix:
13            row.reverse()
14
15        return matrix