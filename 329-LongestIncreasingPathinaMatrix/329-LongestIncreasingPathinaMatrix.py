# Last updated: 8/20/2025, 10:59:15 PM
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dp(i, j):
            best = 1
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[i][j]:
                    best = max(best, 1 + dp(nr, nc))
            return best
        
        return max(dp(i, j) for i in range(m) for j in range(n))