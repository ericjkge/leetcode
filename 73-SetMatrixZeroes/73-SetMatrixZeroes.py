# Last updated: 11/22/2025, 3:05:33 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zeroes = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zeroes = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0
        
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        
        if first_row_zeroes:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_zeroes:
            for r in range(rows):
                matrix[r][0] = 0