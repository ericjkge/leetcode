# Last updated: 1/26/2026, 12:28:47 PM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        rows, cols = len(matrix), len(matrix[0])
7
8        zero_first_row = any(matrix[0][c] == 0 for c in range(cols))
9        zero_first_col = any(matrix[r][0] == 0 for r in range(rows))
10
11        for r in range(rows):
12            for c in range(cols):
13                if matrix[r][c] == 0:
14                    matrix[r][0] = "*"
15                    matrix[0][c] = "*"
16        
17        for r in range(1, rows):
18            if matrix[r][0] == "*":
19                matrix[r][0] = 0
20                for c in range(1, cols):
21                    matrix[r][c] = 0
22
23        for c in range(1, cols):
24            if matrix[0][c] == "*":
25                matrix[0][c] = 0
26                for r in range(1, rows):
27                    matrix[r][c] = 0
28        
29        if zero_first_row:
30            for c in range(cols):
31                matrix[0][c] = 0
32        
33        if zero_first_col:
34            for r in range(rows):
35                matrix[r][0] = 0
36