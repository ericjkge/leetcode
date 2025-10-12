# Last updated: 10/12/2025, 9:59:03 AM
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        INF = 2 ** 31 - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        rows, cols = len(rooms), len(rooms[0])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        moves = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                        rooms[nr][nc] = moves
                        queue.append((nr, nc))
            moves += 1