# Last updated: 10/12/2025, 12:39:42 AM
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)

        queue = deque([(0, 0)])
        seen = set([(0, 0)])
        length = 1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == (n - 1, n - 1):
                    return length
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            length += 1
            
        return -1