# Last updated: 7/20/2025, 4:20:46 PM
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def canCross(day):
            for c in range(col):
                if grid[0][c] == 0 and dfs((0, c)):
                    return True
            return False

        def dfs(node):
            r, c = node
            if r == row - 1:
                return True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen and grid[nr][nc] == 0:
                    seen.add((nr, nc))
                    if dfs((nr, nc)):
                        return True
            return False

        left, right = 0, len(cells)
        while left < right:
            seen = set()
            grid = [[0] * col for _ in range(row)]        
            mid = left + (right - left + 1) // 2
            for x, y in cells[:mid]:
                grid[x - 1][y - 1] = 1
            if canCross(mid):
                left = mid
            else:
                right = mid - 1
        return left
