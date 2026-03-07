# Last updated: 3/7/2026, 11:19:03 AM
1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        rows, cols = len(matrix), len(matrix[0])
7        zero_first_row = any(matrix[0][c] == 0 for c in range(cols))
8        zero_first_col = any(matrix[r][0] == 0 for r in range(rows))
9
10        for r in range(rows):
11            for c in range(cols):
12                if matrix[r][c] == 0:
13                    matrix[r][0] = 0
14                    matrix[0][c] = 0
15
16        for r in range(1, rows):
17            if matrix[r][0] == 0:
18                for c in range(cols):
19                    matrix[r][c] = 0
20        
21        for c in range(1, cols):
22            if matrix[0][c] == 0:
23                for r in range(rows):
24                    matrix[r][c] = 0
25    
26        if zero_first_row:
27            for c in range(cols):
28                matrix[0][c] = 0
29        
30        if zero_first_col:
31            for r in range(rows):
32                matrix[r][0] = 0