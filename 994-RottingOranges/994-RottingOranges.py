# Last updated: 6/24/2025, 5:05:22 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time = fresh = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append([row, col])
                
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append([nx, ny])
                    else:
                        continue
            time += 1

        return time if fresh == 0 else -1
