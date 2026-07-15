# Last updated: 7/15/2026, 12:56:37 AM
1class Solution:
2    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
3        rows, cols = len(matrix), len(matrix[0])
4        r, c = 0, cols - 1
5
6        while r < rows and c >= 0:
7            if matrix[r][c] == target:
8                return True
9            
10            if matrix[r][c] > target:
11                c -= 1
12            else:
13                r += 1
14        
15        return False