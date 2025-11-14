# Last updated: 11/14/2025, 9:40:23 AM
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        arr = [[0] * rows for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                arr[c][r] = matrix[r][c]
        
        return arr