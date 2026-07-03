# Last updated: 7/2/2026, 10:58:22 PM
1class Solution:
2    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
3        rows, cols = len(matrix), len(matrix[0])
4        res = [[0] * rows for _ in range(cols)]
5
6        for r in range(rows):
7            for c in range(cols):
8                res[c][r] = matrix[r][c]
9        
10        return res