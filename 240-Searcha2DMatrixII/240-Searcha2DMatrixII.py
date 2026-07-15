# Last updated: 7/15/2026, 12:53:19 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        rows, cols = len(matrix), len(matrix[0])
4        boundary = None
5        r, c = 0, 0
6
7        while 0 <= r < rows and 0 <= c < cols:
8            if matrix[r][c] == target:
9                return True
10            
11            if matrix[r][c] > target:
12                boundary = c
13                c -= 1
14            else:
15                if boundary is None and c + 1 < cols:
16                    c += 1
17                else:
18                    r += 1
19        
20        return False
21