# Last updated: 6/30/2025, 11:42:58 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = [(sr, sc)]
        original = image[sr][sc]
        image[sr][sc] = color
        seen = set((sr, sc))

        while stack:
            x, y = stack.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(image) and 0 <= ny < len(image[0]) and image[nx][ny] == original and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    stack.append((nx, ny))
                    image[nx][ny] = color
        
        return image
