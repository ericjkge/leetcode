# Last updated: 8/5/2025, 11:02:32 PM
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        rows, cols = len(image), len(image[0])
        self.left, self.right = cols - 1, 0
        self.top, self.bottom = rows - 1, 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()
        
        def dfs(r, c):
            if c > self.right:
                self.right = c
            if c < self.left:
                self.left = c
            if r > self.bottom:
                self.bottom = r
            if r < self.top:
                self.top = r
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen and image[nr][nc] == "1":
                    seen.add((nr, nc))
                    dfs(nr, nc)
        
        seen.add((x, y))
        dfs(x, y)
        
        return (self.right - self.left + 1) * (self.bottom - self.top + 1)