# Last updated: 6/30/2025, 11:49:58 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original = image[sr][sc]
        if original == color:
            return image

        stack = [(sr, sc)]
        while stack:
            x, y = stack.pop()
            image[x][y] = color
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == original:
                    stack.append((nx, ny))
        
        return image
