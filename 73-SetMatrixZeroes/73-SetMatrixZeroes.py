# Last updated: 11/22/2025, 2:34:52 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        def setRow(row):
            for c in range(cols):
                matrix[row][c] = 0
        
        def setCol(col):
            for r in range(rows):
                matrix[r][col] = 0
            
        targets = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    targets.append((r, c))
        
        for r, c in targets:
            setRow(r)
            setCol(c)
        
        return matrix