# Last updated: 8/21/2025, 12:53:33 AM
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    queue.append([row, col])
                    continue
                mat[row][col] = float("inf")

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and mat[nx][ny] > mat[x][y]:
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append([nx, ny])
        return mat